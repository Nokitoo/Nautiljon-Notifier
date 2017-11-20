import logging

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QPropertyAnimation, QSize
from PyQt5.QtGui import QIcon
from gui.notification_ui import Ui_Dialog as NotificationDialog

from config import assets

class Notification(QDialog, NotificationDialog):
    mainWindow = None

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        # Notification offset
        marginBottom = 50.0; # Desktop footer + margin
        marginRight = 20.0;

        # Notification flags
        flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog
        self.setWindowFlags(flags)

        # Set notification at the bottom right of the screen
        screenRect = QApplication.desktop().screenGeometry()
        self.setGeometry(
            screenRect.width() -  self.width() - marginRight,
            screenRect.height() -  self.height() - marginBottom,
             self.width(),
             self.height()
        )


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.deleteLater()

    @staticmethod
    def create(title, message, pixmap):
        if not Notification.mainWindow:
            logging.error('Need to set mainwindow before calling Notification.show()')
            return

        notification = Notification(Notification.mainWindow)
        notification.title.setText(title)
        notification.message.setText(message)

        width = pixmap.width();
        height = pixmap.height();
        notification.icon.setPixmap(pixmap.scaled(width, height, Qt.KeepAspectRatio));

        notification.show()
