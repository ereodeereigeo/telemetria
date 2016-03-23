from PyQt4 import QtGui
from ui.disenos.dialogs import dialog_can_bridge


class EthernetDialog(QtGui.QDialog, dialog_can_bridge.Ui_CanBridgeDialog):

    def __init__(self):
        super(EthernetDialog, self).__init__()
        self.ip = ()
        self.port = 0
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.aceptar_dialogo)
        self.pushButton.clicked.connect(self.cancelar_dialogo)

    def aceptar_dialogo(self):
        self.ip = (self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(), self.spinBox_4.value())
        self.port = self.spinBox_5.value()
        QtGui.QDialog.accept(self)

    def cancelar_dialogo(self):
        QtGui.QDialog.reject(self)