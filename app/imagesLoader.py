import logging
import requests

from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtCore import QSize

from config import assets


class ImagesLoader():
    def __init__(self, sendNotificationCallback):
        super().__init__()

        # Callback to send notification to window thread
        self.sendNotificationCallback = sendNotificationCallback

    def loadImage(self, itemData):
        if itemData['iconUrl'] == 'nautiljon_icon.ico':
            icon = QIcon(assets['nautiljon_icon_desktop'])
            itemData['pixmap'] = icon.pixmap(icon.actualSize(QSize(64, 64)));
        else:
            logging.debug('Loading image %s', itemData['iconUrl'])

            req = requests.get(itemData['iconUrl'], stream=True)

            # Create image
            img = QImage()
            img.loadFromData(req.raw.data)
            itemData['pixmap'] = QPixmap(img)

        # Send callback
        self.sendNotificationCallback(itemData)
