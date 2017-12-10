import logging
import time
from lxml import etree

from PyQt5.QtCore import QObject, pyqtSignal

from imagesLoader import ImagesLoader


class WatcherManager(QObject):
    onNewNotification = pyqtSignal(dict)
    isRunning = True
    # Used to terminate the thread while waiting (safe quit), on app exit
    isWaiting = False

    def __init__(self, watchIntervals):
        super().__init__()
        # Watch interval in minutes
        self.watchIntervals = watchIntervals
        # Store watchers by url
        self.watchers = {}

        # sent items ids mapped with the watcher name
        self.sentItemsIds = {}

    # A new watcher is a dict with the following fields:
    # - name : watcher name, used to store items ids
    # - url : where are the items to search
    # - onNewItem : callback for each new item
    # - newItemsXPath : xpath to search for new items ids
    def addWatcher(self, watcher):
        # Add watcher
        if watcher.url not in self.watchers:
            self.watchers[watcher.url] = []
        self.watchers[watcher.url].append(watcher)

    # Called from imagesLoader when image is loaded
    def sendNotificationCallback(self, itemData):
        self.onNewNotification.emit(itemData)

    def startWatchNotifications(self, user):
        while self.isRunning:
            start = time.time()
            self.watchNotifications(user)

            # Calculate wait time in secs
            # Use max() to prevent elapsedTime from being greater than self.watchIntervals
            end = time.time()
            elapsedTime = end - start
            waitSecs = max(self.watchIntervals * 60 - elapsedTime, 0)

            self.isWaiting = True
            if self.isRunning:
                time.sleep(waitSecs)
            self.isWaiting = False

    def stopWatchNotifications(self):
        self.isRunning = False

    def watchNotifications(self, user):
        # Init images loader
        # We can't create it in __init__ because it should be created
        # in the same thread we are using it
        if not hasattr(self, 'imagesLoader'):
            self.imagesLoader = ImagesLoader(self.sendNotificationCallback)

        for watcherUrl in self.watchers:
            logging.debug('Watching url %s', watcherUrl)
            for watcher in self.watchers[watcherUrl]:
                try:
                    if watcher.enabled == False:
                        continue

                    # Get items page
                    req = user.session.get(watcherUrl)

                    # Parse items
                    tree = etree.HTML(req.text.encode('utf-8'))
                    newItems = tree.xpath(watcher.newItemsXPath)
                    logging.debug('Found new notifications : %s', newItems)

                    # Init items id array
                    itemsIdsKey = watcher.name + '_ids'
                    if not itemsIdsKey in self.sentItemsIds:
                        self.sentItemsIds[itemsIdsKey] = []
                    itemsIds = []

                    for item in newItems:
                        # Retrieve items data
                        itemData = watcher.onNewItem(item)

                        # Only send if not already sent
                        if itemData['itemId'] not in self.sentItemsIds[itemsIdsKey]:
                            logging.debug('Not already sent : %s', itemData)
                            self.imagesLoader.loadImage(itemData)
                        itemsIds.append(itemData['itemId'])

                    # Set items ids as sent
                    self.sentItemsIds[itemsIdsKey] = list(itemsIds)

                except Exception as e:
                    logging.exception('Watcher failed for url %s', watcherUrl)
