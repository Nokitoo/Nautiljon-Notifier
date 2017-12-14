import webbrowser

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal, QEvent
from gui.notification_ui import Ui_Dialog as NotificationDialog

def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                    return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class Notification(QDialog, NotificationDialog):
    queue = []
    notificationDisplayed = None

    def __init__(self, timeout):
        super().__init__()
        self.setupUi(self)
        self.timeout = timeout

        # Notification offset
        marginBottom = 50.0; # Desktop footer + margin
        marginRight = 20.0;

        # Notification flags
        flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool
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
        clickable(self.closeNotification).connect(self.destroyNotification)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and not self.closeNotification.underMouse():
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

        # Don't close notifications if timeout is 0
        if self.timeout != 0:
            self.timer = QTimer()
            self.timer.timeout.connect(self.destroyNotification)
            self.timer.start(self.timeout)


    @staticmethod
    def cleanUp():
        for notification in Notification.queue:
            notification.close()

        if Notification.notificationDisplayed:
            Notification.notificationDisplayed.close()

    @staticmethod
    def create(title, message, pixmap, url, onClick = None, timeout = 5000):
        notification = Notification(timeout)
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
