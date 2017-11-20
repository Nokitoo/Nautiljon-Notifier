import logging
import webbrowser

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QPropertyAnimation, QSize, QTimer
from PyQt5.QtGui import QIcon
from gui.notification_ui import Ui_Dialog as NotificationDialog

from config import assets

class Notification(QDialog, NotificationDialog):
    mainWindow = None
    queue = []
    notificationDisplayed = None

    def __init__(self, parent, timeout):
        super().__init__(parent)
        self.setupUi(self)
        self.timeout = timeout

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

        self.destroyed.connect(self.onNotificationDestroyed)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            webbrowser.open_new_tab(self.url)
            if self.onClick:
                self.onClick()
            self.destroyNotification()

    def onNotificationDestroyed(self):
        Notification.notificationDisplayed = None
        if len(Notification.queue) > 0:
            notification = Notification.queue.pop(0)
            notification.show()
            Notification.notificationDisplayed = notification

    def destroyNotification(self):
        self.destroy()
        self.onNotificationDestroyed()

    def show(self):
        super().show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.destroyNotification)
        self.timer.start(self.timeout)


    @staticmethod
    def cleanUp():
        for notification in Notification.queue:
            notification.destroy()

        if Notification.notificationDisplayed:
            Notification.notificationDisplayed.destroy()

    @staticmethod
    def create(title, message, pixmap, url, onClick = None, timeout = 5000):
        if not Notification.mainWindow:
            logging.error('Need to set mainwindow before calling Notification.show()')
            return

        notification = Notification(Notification.mainWindow, timeout)
        notification.title.setText(title)
        notification.message.setText(message)
        notification.onClick = onClick
        notification.url = url

        width = pixmap.width();
        height = pixmap.height();
        notification.icon.setPixmap(pixmap.scaled(width, height, Qt.KeepAspectRatio));

        if not Notification.notificationDisplayed:
            notification.show()
            Notification.notificationDisplayed = notification
        else:
            Notification.queue.append(notification)
