# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rodrigo/telemetriafinal/telemetria/ui/disenos/designer/dialog_can_bridge.ui'
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

class Ui_CanBridgeDialog(object):
    def setupUi(self, CanBridgeDialog):
        CanBridgeDialog.setObjectName(_fromUtf8("CanBridgeDialog"))
        CanBridgeDialog.resize(296, 151)
        CanBridgeDialog.setMinimumSize(QtCore.QSize(296, 151))
        CanBridgeDialog.setMaximumSize(QtCore.QSize(296, 151))
        self.verticalLayoutWidget = QtGui.QWidget(CanBridgeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(255)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.spinBox_2 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.spinBox_3 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.spinBox_4 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_4.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_4.setMaximum(255)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.horizontalLayout.addWidget(self.spinBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_5 = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_5.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_5.setMaximum(65535)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.horizontalLayout_2.addWidget(self.spinBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(CanBridgeDialog)
        QtCore.QMetaObject.connectSlotsByName(CanBridgeDialog)

    def retranslateUi(self, CanBridgeDialog):
        CanBridgeDialog.setWindowTitle(_translate("CanBridgeDialog", "PUERTO CAN BRIDGE", None))
        self.label.setText(_translate("CanBridgeDialog", "Selecciona IP y puerto ", None))
        self.label_3.setText(_translate("CanBridgeDialog", "IP:", None))
        self.label_2.setText(_translate("CanBridgeDialog", "Puerto: ", None))
        self.pushButton.setText(_translate("CanBridgeDialog", "Cancelar", None))
        self.pushButton_2.setText(_translate("CanBridgeDialog", "Aceptar", None))

