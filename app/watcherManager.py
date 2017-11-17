import logging
from lxml import etree
from PyQt5.QtCore import QObject, pyqtSignal, QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QIcon, QImage, QPixmap


class WatcherManager(QObject):
    onNewNotification = pyqtSignal(dict)

    def __init__(self, watchIntervals):
        super().__init__()
        # Watch interval in seconds
        self.watchIntervals = watchIntervals
        # Store watchers by url
        self.watchers = {}

    # A new watcher is a dict with the following fields:
    # - name : Watcher name, used to store items ids
    # - url
    # - onNewItem : callback for each new notification
    # - newItemsXPath : xpath to search for new notifications ids
    def addWatcher(self, watcher):
        # Check for invalid watcher
        if not 'url' in watcher or not 'onNewItem' in watcher:
            logging.warning('Cannot add a watcher with no url or onNewItem callback')
            return

        # Add watcher
        if watcher['url'] not in self.watchers:
            self.watchers[watcher['url']] = []
        self.watchers[watcher['url']].append(watcher)

    # Send notification to window after loading icon
    def sendNotification(self, itemData):
        logging.debug('Retrieve icon %s', itemData['iconUrl'])

        def imageRetrieved(reply):
            logging.debug('Image retrieved')
            img = QImage()
            img.loadFromData(reply.readAll())
            itemData['icon'] = QIcon(QPixmap(img).scaled(32, 32))
            self.onNewNotification.emit(itemData)

        # Load icon
        self.accessManager = QNetworkAccessManager()
        self.accessManager.finished.connect(imageRetrieved)
        self.accessManager.get(QNetworkRequest(QUrl(itemData['iconUrl'])))

    def run(self, session):
        for watcherUrl in self.watchers:
            logging.debug('Watching url %s', watcherUrl)
            for watcher in self.watchers[watcherUrl]:
                try:
                    req = session.get(watcherUrl)
                    tree = etree.HTML(req.text.encode('utf-8'))
                    newItems = tree.xpath(watcher['newItemsXPath'])
                    logging.debug('Found new notifications : %s', newItems)
                    for item in newItems:
                        itemData = watcher['onNewItem'](item)
                        logging.debug(itemData)
                        self.sendNotification(itemData)
                except Exception as e:
                    logging.error('Watcher failed for url %s : %s', watcherUrl, e)

