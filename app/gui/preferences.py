import sys

from PyQt5.QtWidgets import QDialog

from gui.preferences_ui import Ui_Dialog

class PreferencesDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.startAtBootCheckbox.setChecked(self.parent.settings.contains("Nautiljon Notifier"))

    def onSavePreferences(self):
        if self.startAtBootCheckbox.isChecked():
            self.parent.settings.setValue("Nautiljon Notifier", sys.argv[0]);
        else:
            self.parent.settings.remove("Nautiljon Notifier");
        self.close()

    def onCancel(self):
        self.close()
