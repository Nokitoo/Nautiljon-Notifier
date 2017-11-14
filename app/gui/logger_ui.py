# Python core libraries
import logging

# PyQT5 files
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QPushButton, QVBoxLayout

class LoggerHandler(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class LoggerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create logger handler
        logTextBox = LoggerHandler(self)
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        # Add logger handler to python handlers
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)

        # Add logger to layout
        layout = QVBoxLayout()
        layout.addWidget(logTextBox.widget)
        self.setLayout(layout)
