# Python core libraries
import logging

# PyQT5 files
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal

class LoggerHandler(QObject, logging.Handler):
    log = pyqtSignal(logging.Handler, logging.LogRecord)

    def __init__(self, parent):
        super(LoggerHandler, self).__init__()
        self.parent = parent


    # Emit is called when a log function is called (Ex: logging.debug)
    def emit(self, record):
        # Send log to UI thread
        self.log.emit(self, record)

class LoggerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create logger handler
        logTextBox = LoggerHandler(self)
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        # Add the log received from LoggerHandler.emit
        def addLogToBox(logger, record):
            msg = logger.format(record)
            self.widget.appendPlainText(msg)

        logTextBox.log.connect(addLogToBox)

        # Add logger handler to python handlers
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.DEBUG)

        # Add logger box to layout
        layout = QVBoxLayout()
        self.widget = QPlainTextEdit(parent)
        layout.addWidget(self.widget)
        self.setLayout(layout)

        self.widget.setReadOnly(True)
