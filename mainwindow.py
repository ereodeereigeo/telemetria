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
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui
from ui.disenos.mainwindow import mainwindow
from ui.dialogs.DialogEthernet import EthernetDialog
from ui.dialogs.DialogSerial import SerialDialog


class MainWindow (QtGui.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.ip = ()
        self.port = ()
        self.com = ()
        self.thread_serial = ThreadSerial()
        self.thread_wifi = ThreadSocketUDP()

        # senales botones

        self.conectarWifi.clicked.connect(self.get_config_wifi)
        self.conectarXBee.clicked.connect(self.get_config_serial)

        # senales threads

        self.checkBoxXbee.clicked.connect(self.iniciar_comunicaciones_serial)
        self.thread_serial.serial_signal.connect(self.recivir_data_serial)
        self.thread_serial.finished.connect(self.serial_terminado)

        self.checkBoxWifi.clicked.connect(self.iniciar_comunicaciones_wifi)
        self.thread_wifi.udp_signal.connect(self.recivir_data_wifi)
        self.thread_wifi.finished.connect(self.recivir_data_wifi)

    def iniciar_comunicaciones_serial(self):
        if not self.thread_serial.alive:
            self.thread_serial.start()
        else:
            self.thread_serial.alive = False

    def iniciar_comunicaciones_wifi(self):
        if not self.thread_wifi.alive:
            self.thread_wifi.start()
        else:
            self.thread_wifi.alive = False

    def get_config_serial(self):
        dialogo_serial = SerialDialog()
        if dialogo_serial.exec_():
            print('dialgo_serial', dialogo_serial.com)
            self.com = dialogo_serial.com

    def get_config_wifi(self):
        dialgo_wifi = EthernetDialog()
        if dialgo_wifi.exec_():
            print('dialogo_ethernet', 'ip:', dialgo_wifi.ip, 'puerto:', dialgo_wifi.port)
            self.ip = dialgo_wifi.ip
            self.port = dialgo_wifi.port

    @QtCore.pyqtSlot(dict)
    def recivir_data_wifi(self, data):
        print(data)

    @QtCore.pyqtSlot(dict)
    def recivir_data_serial(self, data):

        print(data)

    def serial_terminado(self):
        pass

    def wifi_terminado(self):
        pass


class ThreadSerial(QtCore.QThread):
    serial_signal = QtCore.pyqtSignal(dict)

    def __init__(self):
        super(ThreadSerial, self).__init__()
        self.alive = False

    def configurar(self, parametros):
        pass

    @QtCore.pyqtSlot()
    def detener_thread(self):
        self.alive = False

    def run(self):
        self.alive = True
        while self.alive:
            data_salida = dict(string='THREAD SERIAL', hora=datetime.datetime.now())
            self.serial_signal.emit(data_salida)
            time.sleep(1)


class ThreadSocketUDP(QtCore.QThread):
    udp_signal = QtCore.pyqtSignal(dict)

    def __init__(self):
        super(ThreadSocketUDP, self).__init__()
        self.alive = False

    def configurar(self, parametros):
        pass

    @QtCore.pyqtSlot()
    def detener_thread(self):
        self.alive = False

    def run(self):
        self.alive = True
        while self.alive:
            data_salida = dict(string='THREAD SOCKET UDP', hora=datetime.datetime.now())
            self.udp_signal.emit(data_salida)
            time.sleep(1)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
