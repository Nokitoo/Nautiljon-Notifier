import sys

from PyQt5.QtWidgets import QDialog

from gui.preferences_ui import Ui_Dialog

class PreferencesDialog(QDialog, Ui_Dialog):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user

        self.setupUi(self)
        self.startAtBootCheckbox.setChecked(self.user.settings.startAtBoot)
        self.notificationsCheckbox.setChecked(self.user.settings.notifications)
        self.messagesCheckbox.setChecked(self.user.settings.messages)

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

        if changed:
            self.user.updateWatchers()
            self.user.saveData()

    def onCancel(self):
        self.close()
