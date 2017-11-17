# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nokito\Documents\Nautiljon Notifier PythonQT\scripts\../app/gui\window.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.loginForm = QtWidgets.QWidget(self.centralWidget)
        self.loginForm.setGeometry(QtCore.QRect(110, 0, 251, 91))
        self.loginForm.setObjectName("loginForm")
        self.formLayout = QtWidgets.QFormLayout(self.loginForm)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.loginForm)
        self.usernameLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.usernameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameInput = QtWidgets.QLineEdit(self.loginForm)
        self.usernameInput.setObjectName("usernameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameInput)
        self.passwordLabel = QtWidgets.QLabel(self.loginForm)
        self.passwordLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.passwordLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordInput = QtWidgets.QLineEdit(self.loginForm)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.connectButton = QtWidgets.QPushButton(self.loginForm)
        self.connectButton.setObjectName("connectButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connectButton)
        self.connectError = QtWidgets.QLabel(self.centralWidget)
        self.connectError.setEnabled(True)
        self.connectError.setGeometry(QtCore.QRect(110, 100, 251, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.connectError.setFont(font)
        self.connectError.setStyleSheet("QLabel { color : red; }")
        self.connectError.setAlignment(QtCore.Qt.AlignCenter)
        self.connectError.setObjectName("connectError")
        self.connectSuccess = QtWidgets.QLabel(self.centralWidget)
        self.connectSuccess.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.connectSuccess.setStyleSheet("QLabel { color : green; }")
        self.connectSuccess.setObjectName("connectSuccess")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setEnabled(True)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.connectButton.clicked.connect(MainWindow.onConnect)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nautiljon notifier"))
        self.usernameLabel.setText(_translate("MainWindow", "Identifiant"))
        self.passwordLabel.setText(_translate("MainWindow", "Mot de passe"))
        self.connectButton.setText(_translate("MainWindow", "Se connecter"))
        self.connectError.setText(_translate("MainWindow", "Mauvais identifiants"))
        self.connectSuccess.setText(_translate("MainWindow", "Vous êtes connecté"))

