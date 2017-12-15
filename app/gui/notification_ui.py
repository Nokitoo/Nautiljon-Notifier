# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nokito\Documents\Nautiljon Notifier PythonQT\scripts\../app/gui\notification.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 120)
        Dialog.setWindowOpacity(1.0)
        Dialog.setToolTip("")
        Dialog.setStyleSheet("*{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QDialog {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"#closeNotification {\n"
"    background-color: transparent;\n"
"}")
        self.icon = QtWidgets.QLabel(Dialog)
        self.icon.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.icon.setStyleSheet("")
        self.icon.setText("")
        self.icon.setScaledContents(False)
        self.icon.setObjectName("icon")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 20, 231, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.PlainText)
        self.title.setScaledContents(False)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.message = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.closeNotification = QtWidgets.QLabel(Dialog)
        self.closeNotification.setGeometry(QtCore.QRect(340, 0, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.closeNotification.setFont(font)
        self.closeNotification.setAlignment(QtCore.Qt.AlignCenter)
        self.closeNotification.setObjectName("closeNotification")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "TextLabel"))
        self.message.setText(_translate("Dialog", "TextLabel"))
        self.closeNotification.setText(_translate("Dialog", "x"))

