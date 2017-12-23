import sys
import os

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIntValidator

from gui.preferences_ui import Ui_Dialog

class PreferencesDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user

        self.setupUi(self)
        self.startAtBootCheckbox.setChecked(self.user.settings.startAtBoot)
        self.notificationsCheckbox.setChecked(self.user.settings.notifications)
        self.messagesCheckbox.setChecked(self.user.settings.messages)
        self.notificationsCloseSeconds.setText(str(self.user.settings.notificationsCloseSeconds))

        self.notificationsCloseSeconds.setValidator(QIntValidator(0, 100, self));

        # Hide "start at boot" option if not on windows
        if os.name != 'nt':
            self.startAtBootCheckbox.hide()

    def onSavePreferences(self):
        self.close()

        changed = self.user.settings.notifications != self.notificationsCheckbox.isChecked() or\
            self.user.settings.messages != self.messagesCheckbox.isChecked() or\
            self.user.settings.startAtBoot != self.startAtBootCheckbox.isChecked()

        if self.startAtBootCheckbox.isChecked():
            self.user.settings.settings.setValue("Nautiljon Notifier", sys.argv[0]);
        else:
            self.user.settings.settings.remove("Nautiljon Notifier");

        self.user.settings.notifications = self.notificationsCheckbox.isChecked()
        self.user.settings.messages = self.messagesCheckbox.isChecked()
        self.user.settings.startAtBoot = self.startAtBootCheckbox.isChecked()
        self.user.settings.notificationsCloseSeconds = int(self.notificationsCloseSeconds.text())

        if changed:
            self.user.updateWatchers()
            self.user.saveData()

    def onCancel(self):
        self.close()
