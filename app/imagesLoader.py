import logging
import requests

from PyQt5.QtGui import QIcon, QImage, QPixmap

from config import assets


class ImagesLoader():
    def __init__(self, sendNotificationCallback):
        super().__init__()

        # Map QNetworkRequest requests with their corresponding itemData
        self.replies = {}

        # Callback to send notification to window thread
        self.sendNotificationCallback = sendNotificationCallback

    def loadImage(self, itemData):
        logging.debug('Loading image %s', itemData['iconUrl'])

        req = requests.get(itemData['iconUrl'], stream=True)

        # Create image
        img = QImage()
        img.loadFromData(req.raw.data)
        itemData['icon'] = QIcon(QPixmap(img).scaled(32, 32))

        # Send callback
        self.sendNotificationCallback(itemData)
