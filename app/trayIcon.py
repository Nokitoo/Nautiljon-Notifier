from PyQt5.QtWidgets import QSystemTrayIcon, QMenu
from PyQt5.QtCore import Qt

class TrayIcon(QSystemTrayIcon):
    def __init__(self, window, icon):
        super().__init__(icon)
        self.window = window

        menu = QMenu();

        openAction = menu.addAction('ouvrir');
        quitAction = menu.addAction('quitter');

        openAction.triggered.connect(self.window.show);
        quitAction.triggered.connect(self.quitActionTriggered);

        self.activated.connect(self.trayIconActivated)
        self.setContextMenu(menu)
        self.show()

    def trayIconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.window.show()

    def quitActionTriggered(self, checked):
        self.window.closeWindow = True
        self.window.close()
