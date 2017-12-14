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
        Dialog.resize(475, 266)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(280, 230, 75, 23))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(370, 230, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 171, 91))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 121, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.notificationsCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.notificationsCheckbox.setObjectName("notificationsCheckbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.notificationsCheckbox)
        self.messagesCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.messagesCheckbox.setObjectName("messagesCheckbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.messagesCheckbox)
        self.startAtBootCheckbox = QtWidgets.QCheckBox(Dialog)
        self.startAtBootCheckbox.setGeometry(QtCore.QRect(20, 20, 125, 17))
        self.startAtBootCheckbox.setObjectName("startAtBootCheckbox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 180, 341, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.notificationsCloseSeconds = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.notificationsCloseSeconds.setObjectName("notificationsCloseSeconds")
        self.horizontalLayout.addWidget(self.notificationsCloseSeconds)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Dialog)
        self.okButton.clicked.connect(Dialog.onSavePreferences)
        self.cancelButton.clicked.connect(Dialog.onCancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Préférences"))
        self.okButton.setText(_translate("Dialog", "Ok"))
        self.cancelButton.setText(_translate("Dialog", "Annuler"))
        self.groupBox.setTitle(_translate("Dialog", "Recevoir des notifications pour:"))
        self.notificationsCheckbox.setText(_translate("Dialog", "Notifications"))
        self.messagesCheckbox.setText(_translate("Dialog", "Messages"))
        self.startAtBootCheckbox.setText(_translate("Dialog", "Lancer au démarrage"))
        self.label.setText(_translate("Dialog", "Fermer automatiquement les notifications après"))
        self.label_2.setText(_translate("Dialog", "secondes"))

