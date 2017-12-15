# Python core libraries
import os
import logging

# PyQT5 files
from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSignal

from config import config
from decorators import autoCreateDir


class LoggerHandler(QObject, logging.Handler):
    log = pyqtSignal(logging.Handler, logging.LogRecord)

    def __init__(self, parent):
        super(LoggerHandler, self).__init__()
        self.parent = parent


    # Emit is called when a log function is called (Ex: logging.debug)
    def emit(self, record):
        # Send log to LoggerDialog (Because we can log from non-UI thread)
        self.log.emit(self, record)

class LoggerDialog(QDialog):
    @autoCreateDir(config['data_dir_path'])
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create logger handler
        textBoxHandler = LoggerHandler(self)
        textBoxHandler.setFormatter(logging.Formatter(u'%(asctime)s - %(levelname)s - %(message)s'))

        # Create file handler
        fileHandler = logging.FileHandler(os.path.join(config['data_dir_path'], "logs.txt"))
        fileHandler.setFormatter(logging.Formatter(u'%(asctime)s - %(levelname)s - %(message)s'))

        # Add the log received from LoggerHandler.emit
        def addLogToBox(logger, record):
            msg = logger.format(record)
            self.widget.appendPlainText(msg)

        # Connect text box handler to UI
        textBoxHandler.log.connect(addLogToBox)

        # Add logger handlers (text box + file)
        logging.getLogger().addHandler(textBoxHandler)
        logging.getLogger().addHandler(fileHandler)
        logging.getLogger().setLevel(logging.DEBUG)

        # Add logger text box to layout
        layout = QVBoxLayout()
        self.widget = QPlainTextEdit(parent)
        layout.addWidget(self.widget)
        self.setLayout(layout)

        self.widget.setReadOnly(True)
