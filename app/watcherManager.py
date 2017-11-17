import logging
from lxml import etree
from PyQt5.QtCore import QObject, pyqtSignal

from imagesLoader import ImagesLoader


class WatcherManager(QObject):
    onNewNotification = pyqtSignal(dict)

    def __init__(self, watchIntervals):
        super().__init__()
        # Watch interval in seconds
        self.watchIntervals = watchIntervals
        # Store watchers by url
        self.watchers = {}

    # A new watcher is a dict with the following fields:
    # - name : watcher name, used to store items ids
    # - url : where are the items to search
    # - onNewItem : callback for each new item
    # - newItemsXPath : xpath to search for new items ids
    def addWatcher(self, watcher):
        # Check for invalid watcher
        if not 'url' in watcher or not 'onNewItem' in watcher:
            logging.warning('Cannot add a watcher with no url or onNewItem callback')
            return

        # Add watcher
        if watcher['url'] not in self.watchers:
            self.watchers[watcher['url']] = []
        self.watchers[watcher['url']].append(watcher)

    # Called from imagesLoader when image is loaded
    def sendNotificationCallback(self, itemData):
        self.onNewNotification.emit(itemData)

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
                    req = user.session.get(watcherUrl)
                    tree = etree.HTML(req.text.encode('utf-8'))
                    newItems = tree.xpath(watcher['newItemsXPath'])
                    logging.debug('Found new notifications : %s', newItems)
                    for item in newItems:
                        itemData = watcher['onNewItem'](item)
                        logging.debug(itemData)
                        self.imagesLoader.loadImage(itemData)
                except Exception as e:
                    logging.error('Watcher failed for url %s : %s', watcherUrl, e)

