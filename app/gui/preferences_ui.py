# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nokito\Documents\Nautiljon Notifier PythonQT\scripts\../app/gui\preferences.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 187)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(260, 150, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 20, 181, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.startAtBootCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.startAtBootCheckbox.setObjectName("startAtBootCheckbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startAtBootCheckbox)

        self.retranslateUi(Dialog)
        self.okButton.clicked.connect(Dialog.onSavePreferences)
        self.cancelButton.clicked.connect(Dialog.onCancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Préférences"))
        self.okButton.setText(_translate("Dialog", "Ok"))
        self.cancelButton.setText(_translate("Dialog", "Annuler"))
        self.startAtBootCheckbox.setText(_translate("Dialog", "Lancer au démarrage"))

