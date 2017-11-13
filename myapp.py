import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QSystemTrayIcon
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)


        self.systemtray_icon = QSystemTrayIcon(QIcon('nautiljon_icon.ico'))
        self.systemtray_icon.show()
        # systemtray_icon.showMessage('Title', 'Content', QIcon('nautiljon_icon.ico'))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
