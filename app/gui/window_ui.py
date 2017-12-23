# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nokito/Documents/testVirtualEnv/Nautiljon-Notifier/scripts/../app/gui/window.ui'
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
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.loadingSpinner = QtWidgets.QLabel(self.centralWidget)
        self.loadingSpinner.setGeometry(QtCore.QRect(230, 100, 41, 41))
        self.loadingSpinner.setScaledContents(True)
        self.loadingSpinner.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingSpinner.setObjectName("loadingSpinner")
        self.formContainer = QtWidgets.QFrame(self.centralWidget)
        self.formContainer.setGeometry(QtCore.QRect(70, 30, 331, 201))
        self.formContainer.setStyleSheet("QFrame {\n"
"    border: 0;\n"
"}")
        self.formContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.formContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.formContainer.setObjectName("formContainer")
        self.connectSuccess = QtWidgets.QLabel(self.formContainer)
        self.connectSuccess.setGeometry(QtCore.QRect(130, 90, 151, 21))
        self.connectSuccess.setStyleSheet("QLabel { color : green; }")
        self.connectSuccess.setObjectName("connectSuccess")
        self.loginForm = QtWidgets.QWidget(self.formContainer)
        self.loginForm.setGeometry(QtCore.QRect(40, 60, 251, 91))
        self.loginForm.setObjectName("loginForm")
        self.formLayout = QtWidgets.QFormLayout(self.loginForm)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
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
        self.connectError = QtWidgets.QLabel(self.formContainer)
        self.connectError.setEnabled(True)
        self.connectError.setGeometry(QtCore.QRect(50, 150, 233, 13))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.connectError.setFont(font)
        self.connectError.setStyleSheet("QLabel { color : red; }")
        self.connectError.setAlignment(QtCore.Qt.AlignCenter)
        self.connectError.setObjectName("connectError")
        self.formContainer.raise_()
        self.loadingSpinner.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFichier.addAction(self.actionQuit)
        self.menuOptions.addAction(self.actionPreferences)
        self.menuBar.addAction(self.menuFichier.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.connectButton.clicked.connect(MainWindow.onConnect)
        self.actionQuit.triggered['bool'].connect(MainWindow.onActionQuit)
        self.actionPreferences.triggered['bool'].connect(MainWindow.onActionPreferences)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nautiljon Notifier"))
        self.loadingSpinner.setText(_translate("MainWindow", "TextLabel"))
        self.connectSuccess.setText(_translate("MainWindow", "Vous êtes connecté"))
        self.usernameLabel.setText(_translate("MainWindow", "Identifiant"))
        self.passwordLabel.setText(_translate("MainWindow", "Mot de passe"))
        self.connectButton.setText(_translate("MainWindow", "Se connecter"))
        self.connectError.setText(_translate("MainWindow", "Mauvais identifiants"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionQuit.setText(_translate("MainWindow", "Quitter"))
        self.actionPreferences.setText(_translate("MainWindow", "Préférences"))

