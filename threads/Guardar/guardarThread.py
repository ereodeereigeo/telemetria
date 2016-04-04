from PyQt4 import QtCore

class GuardarThread(QtCore.QThread):
    def __init__(self):
        super(GuardarThread, self).__init__()