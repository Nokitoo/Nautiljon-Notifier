import logging

from PyQt5.QtCore import QSettings

RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"

class UserSettings():
    def __init__(self):
        self.settings = QSettings(RUN_PATH, QSettings.NativeFormat)

        self.startAtBoot = self.settings.contains("Nautiljon Notifier")
        self.notifications = True
        self.messages = True

    def loadFromJson(self, userDataJson):
        logging.debug('Loading user settings')
        try:
            self.notifications = userDataJson['settings']['notifications']
            self.messages = userDataJson['settings']['messages']
        except Exception as e:
            logging.exception('Failed to load user settings')
