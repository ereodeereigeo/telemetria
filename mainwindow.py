from PyQt4 import uic
from PyQt4 import QtCore, QtGui
import socket
#from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import codecs
#from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import struct
import binascii
from collections import deque
#import serial
import time
import datetime
import pandas as pd

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class udpThread(QtCore.QThread):
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


class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )

    def on_conectarWifi_pressed(self):
        self.ui.checkBoxWifi.setChecked(True)
        self.start_udpThread()

    def start_udpThread(self):
        global udp
        multicast_group = '239.255.60.60'
        server_address = ('', 4876)
        udp = udpThread(multicast_group, server_address)
        udp.start()
        self.connect(udp, self.updateUi())





    def __del__ ( self ):
        self.ui = None



