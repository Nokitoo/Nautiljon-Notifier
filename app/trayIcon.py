from PyQt5.QtWidgets import QSystemTrayIcon, QMenu

class TrayIcon(QSystemTrayIcon):
    def __init__(self, window, icon):
        super().__init__(icon)
        self.window = window

        menu = QMenu();

        openAction = menu.addAction('ouvrir');
        quitAction = menu.addAction('quitter');

        openAction.triggered.connect(self.window.show);
        quitAction.triggered.connect(self.window.onActionQuit);

        self.activated.connect(self.trayIconActivated)
        self.setContextMenu(menu)
        self.show()

    def trayIconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.window.show()
