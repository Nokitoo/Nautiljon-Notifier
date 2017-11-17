import logging

from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtGui import QIcon, QImage, QPixmap


class ImagesLoader(QNetworkAccessManager):
    def __init__(self, sendNotificationCallback):
        super().__init__()

        # Map QNetworkRequest requests with their corresponding itemData
        self.replies = {}

        self.finished.connect(self.imageRetrieved)

        # Callback to send notification to window thread
        self.sendNotificationCallback = sendNotificationCallback

    # Image retrieved from QNetworkAccessManager
    def imageRetrieved(self, reply):
        if reply not in self.replies:
            logging.error('Cannot find reply in ImagesLoader.replies')
            return;

        # Retrieve itemData from replies and delete its key
        itemData = self.replies[reply]
        self.replies.pop(reply)

        logging.debug('Icon %s retrieved', itemData['iconUrl'])

        # Load image
        img = QImage()
        img.loadFromData(reply.readAll())
        itemData['icon'] = QIcon(QPixmap(img).scaled(32, 32))

        # Send notification to window thread
        self.sendNotificationCallback(itemData)

    def loadImage(self, itemData):
        request = QNetworkRequest(QUrl(itemData['iconUrl']))
        reply = self.get(request)

        self.replies[reply] = itemData
