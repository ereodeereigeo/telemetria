# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rodrigo/telemetriafinal/telemetria/ui/disenos/designer/dialog_puerto_com.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SerialDialog(object):
    def setupUi(self, SerialDialog):
        SerialDialog.setObjectName(_fromUtf8("SerialDialog"))
        SerialDialog.resize(256, 154)
        SerialDialog.setMinimumSize(QtCore.QSize(256, 154))
        SerialDialog.setMaximumSize(QtCore.QSize(256, 154))
        self.verticalLayoutWidget_2 = QtGui.QWidget(SerialDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 251, 131))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelar = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.horizontalLayout.addWidget(self.cancelar)
        self.aceptar = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.aceptar.setObjectName(_fromUtf8("aceptar"))
        self.horizontalLayout.addWidget(self.aceptar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SerialDialog)
        QtCore.QMetaObject.connectSlotsByName(SerialDialog)

    def retranslateUi(self, SerialDialog):
        SerialDialog.setWindowTitle(_translate("SerialDialog", "PUERTO COM", None))
        self.label.setText(_translate("SerialDialog", "Seleccione el puerto", None))
        self.cancelar.setText(_translate("SerialDialog", "cancelar", None))
        self.aceptar.setText(_translate("SerialDialog", "aceptar", None))

