import glob
import sys
import serial
from PyQt4 import QtGui
from ui.disenos.dialogs import dialog_puerto_com


class SerialDialog(QtGui.QDialog, dialog_puerto_com.Ui_SerialDialog):

    def __init__(self):
        super(SerialDialog, self).__init__()
        self.setupUi(self)
        self.setup_list_of_ports()
        self.cancelar.clicked.connect(self.cancelar_dialog)
        self.aceptar.clicked.connect(self.aceptar_dialog)
        self.com = ''

    def setup_list_of_ports(self):
        plataforma = sys.platform

        if plataforma.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        else:
            ports = glob.glob('/dev/tty[A-Za-z]*')
        result = []

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except(OSError, serial.SerialException):
                pass
        self.comboBox.clear()
        self.comboBox.addItems(result)

    def cancelar_dialog(self):
        QtGui.QDialog.reject(self)

    def aceptar_dialog(self):
        self.com = self.comboBox.currentText()
        QtGui.QDialog.accept(self)