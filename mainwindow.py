from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import socket
import codecs
import numpy as np
import struct
import binascii
from collections import deque
# import serial
import time
import datetime
import pandas as pd
from ui.disenos.mainwindow import mainwindow
from ui.dialogs.DialogEthernet import EthernetDialog
from ui.dialogs.DialogSerial import SerialDialog


class MainWindow (QtGui.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.conectarWifi.clicked.connect(self.get_config_wifi)
        self.conectarXBee.clicked.connect(self.get_config_serial)

    def get_config_serial(self):
        dialogo_serial = SerialDialog()
        if dialogo_serial.exec_():
            print('dialgo_serial', dialogo_serial.com)

    def get_config_wifi(self):
        dialgo_wifi = EthernetDialog()
        if dialgo_wifi.exec_():
            print('dialogo_ethernet')


class ThreadSerial(QtCore.QThread):
    udp_signal = QtCore.pyqtSignal()

    def __init__(self, multicast_group, server_address):
        QtCore.QThread.__init__(self)
        self.multicast_group = multicast_group
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(server_address)
        self.group = socket.inet_aton(self.multicast_group)
        self.mreq = struct.pack('4sL', self.group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, self.mreq)

    def __del__(self):
        self.wait()

    def run(self):
        self.data, self.address = self.sock.recvfrom(1024)
        self.udp_signal.emit()
        print(self.data)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
