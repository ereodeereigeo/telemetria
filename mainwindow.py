import socket
import codecs
import numpy as np
import struct
import binascii
from collections import deque
# import serial
import time
import datetime
import dicc_variables2
import dicc_nuevo
import decodificacion as dec
import pandas as pd
import pyqtgraph as pg
import binascii
from PyQt4 import QtCore, QtGui
from ui.disenos.mainwindow import mainwindow
from ui.dialogs.DialogEthernet import EthernetDialog
from ui.dialogs.DialogSerial import SerialDialog
global previous, diccionario_nuevo, diccionario_final, dataframe_timestamp, dataframe_global
previous = time.time()
diccionario_nuevo = dicc_nuevo.diccionario_nuevo
diccionario_final = {}
dataframe_timestamp = pd.DataFrame(columns=diccionario_nuevo.keys())
dataframe_global = pd.DataFrame(columns=diccionario_nuevo.keys())
pg.setConfigOption('background', 'w')
color1 = (15, 45, 106)
color2 = (127, 143, 175)
color3 = (215, 12, 12)
color4 = (255, 128, 128)
color5 = (0, 32, 96)
color6 = (0, 174, 75)
color7 = (255, 0, 0)
color8 = (0, 175, 77)



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
        self.thread_serial.serial_signal.connect(self.recibir_data_serial)
        self.thread_serial.finished.connect(self.serial_terminado)

        self.checkBoxWifi.clicked.connect(self.iniciar_comunicaciones_wifi)
        self.thread_wifi.udp_signal.connect(self.recibir_data_wifi)
        self.thread_wifi.finished.connect(self.recibir_data_wifi)

        layout_izquierda_1 = QtGui.QVBoxLayout()
        layout_izquierda_2 = QtGui.QVBoxLayout()
        layout_izquierda_3 = QtGui.QVBoxLayout()

        self.plot_izquierda_1 = pg.PlotWidget()
        self.plot_izquierda_2 = pg.PlotWidget()
        self.plot_izquierda_3 = pg.PlotWidget()
        self.curva1 = self.plot_izquierda_1.plot(pen=color1)
        self.curva1_1 = self.plot_izquierda_1.plot(pen=color2)
        self.curva2 = self.plot_izquierda_2.plot(pen=color2)
        self.curva3 = self.plot_izquierda_3.plot(pen=color3)

        layout_izquierda_1.addWidget(self.plot_izquierda_1)
        layout_izquierda_2.addWidget(self.plot_izquierda_2)
        layout_izquierda_3.addWidget(self.plot_izquierda_3)

        self.graphicsView.setLayout(layout_izquierda_1)
        self.graphicsView_2.setLayout(layout_izquierda_2)
        self.graphicsView_3.setLayout(layout_izquierda_3)

        layout_derecha_1 = QtGui.QVBoxLayout()
        layout_derecha_2 = QtGui.QVBoxLayout()
        layout_derecha_3 = QtGui.QVBoxLayout()

        self.plot_derecha_4 = pg.PlotWidget()
        self.plot_derecha_5 = pg.PlotWidget()
        self.plot_derecha_6 = pg.PlotWidget()
        self.curva4 = self.plot_derecha_4.plot(pen=color1)
        self.curva4_1 = self.plot_derecha_4.plot(pen=color2)
        self.curva5 = self.plot_derecha_5.plot(pen=color5)
        self.curva6 = self.plot_derecha_6.plot(pen=color6)

        layout_derecha_1.addWidget(self.plot_derecha_4)
        layout_derecha_2.addWidget(self.plot_derecha_5)
        layout_derecha_3.addWidget(self.plot_derecha_6)

        self.graphicsView_4.setLayout(layout_derecha_1)
        self.graphicsView_5.setLayout(layout_derecha_2)
        self.graphicsView_6.setLayout(layout_derecha_3)

        self.guardar_bitacora_1.pressed.connect(self.guardar_en_bitacora_1)
        self.guardar_bitacora_2.pressed.connect(self.guardar_en_bitacora_2)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()



    def displayTime(self):
        self.hora_bitacora_1.setDateTime(QtCore.QDateTime.currentDateTime())
        self.hora_bitacora_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.fecha.setDateTime(QtCore.QDateTime.currentDateTime())

    def guardar_en_bitacora_1(self):
        self.bitacora_1.append(self.hora_bitacora_1.text())
        self.bitacora_1.append(self.insert_on_bitacora_1.toHtml())
        self.bitacora_1.append('')
        self.insert_on_bitacora_1.setText('')
        self.bitacora_2.setText(self.bitacora_1.toHtml())

    def guardar_en_bitacora_2(self):
        self.bitacora_2.append(self.hora_bitacora_2.text())
        self.bitacora_2.append(self.insert_on_bitacora_2.toHtml())
        self.bitacora_2.append('')
        self.insert_on_bitacora_2.setText('')
        self.bitacora_1.setText(self.bitacora_2.toHtml())

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
        dialogo_wifi = EthernetDialog()
        if dialogo_wifi.exec_():
            print('dialogo_ethernet', 'ip:', dialogo_wifi.ip, 'puerto:', dialogo_wifi.port)
            self.ip = dialogo_wifi.ip
            self.port = dialogo_wifi.port

    def setup_grafico_izquierda(self):
        pass

    def setup_grafico_derecha(self):
        pass


    @QtCore.pyqtSlot(dict)
    def recibir_data_wifi(self, data):
        global previous, diccionario_nuevo, diccionario_final, dataframe_timestamp, dataframe_global
        hexdata = binascii.hexlify(data['data'])
        listaid = []
        inicio = 37
        fin = 40
        ident = '0'
        inicio_datos = 44
        fin_datos = inicio_datos + 16
        lista_datos = []
        while len(ident)>0:
            ident = hexdata[inicio:fin]
            datos = hexdata[inicio_datos:fin_datos]
            if ident in dicc_variables2.dicc_variables.keys():
                listaid.append(ident)
                lista_datos.append(datos)
            inicio = inicio + 28
            inicio_datos = inicio_datos + 28
            fin_datos = fin_datos +28
            fin = fin + 28
        '''for x in listaid:
            if x == b'6f9':
                print (hexdata)'''
        for indice in range(len(listaid)):
            inicio_dato = 0
            try:
                #print('bien')
                for elemento in dicc_variables2.dicc_variables[listaid[indice]]:
                    fin_dato = inicio_dato + elemento[1]
                    dato = lista_datos[indice][inicio_dato:fin_dato]
                    #invertir dato
                    n = 2
                    dato_der = [dato[i : i+n] for i in range(0,len(dato),n)]
                    dato_inv = b''.join(dato_der[::-1])
                    if dato_inv == b'':
                        pass
                    else:
                        if elemento[2] == 'uint32':
                            dato_conv = dec.uint32(dato_inv)
                        elif elemento[2] == 'int32':
                            dato_conv = dec.int32(dato_inv)
                        elif elemento[2] == 'uint16':
                            dato_conv = dec.uint16(dato_inv)
                        elif elemento[2] == 'int16':
                            dato_conv = dec.int16(dato_inv)
                        elif elemento[2] == 'float32':
                            dato_conv = dec.float32(dato_inv)
                        elif elemento[2] == 'uint8':
                            dato_conv = dec.uint8(dato_inv)
                        elif elemento[2] == 'int8':
                            dato_conv = dec.int8(dato_inv)
                        elif elemento[2] == 'data_u32':
                            dato_conv = dec.data_u32(dato_inv)
                        elif elemento[2] == 'data_32':
                            dato_conv = dec.data_32(dato_inv)
                        elif elemento[2] == 'nada':
                            dato_conv = 0.0
                        elif elemento[2] == 'despues':
                            dato_conv = 0.0
                        else:
                            inicio_dato = 0
                            dato_conv = 0
                        diccionario_nuevo[elemento[0]].append(dato_conv)
                        inicio_dato = inicio_dato+ elemento[1]

            except KeyError:
                #print('keyError')
                pass
        tiempo_actual = time.time()
        if (tiempo_actual - previous >= 1):
            previous = tiempo_actual
            for elemento in diccionario_nuevo.keys():
                    if len(diccionario_nuevo[elemento])>0:
                        if (elemento == 'limit_flags_m1') or (elemento == 'limit_flags_m2')\
                                or (elemento == 'error_flags_m1') or (elemento == 'error_flags_m2'):
                            diccionario_final[elemento] = max(diccionario_nuevo[elemento])
                            diccionario_nuevo[elemento] = []
                        else:
                            diccionario_final[elemento] = [sum(diccionario_nuevo[elemento])/len(diccionario_nuevo[elemento])]
                            diccionario_nuevo[elemento] = []
                    else:
                        diccionario_final[elemento] = [float('nan')]
                        diccionario_nuevo[elemento] = []
            diccionario_nuevo = dicc_nuevo.diccionario_nuevo
            dataframe_timestamp = pd.DataFrame(diccionario_final, index =[datetime.datetime.now().replace(microsecond = 0)] )
            dataframe_global = dataframe_global.append(dataframe_timestamp)
            # Asignar velocidad actual
            self.vel_actual_1.setValue(dataframe_timestamp.velocity_ms_m1*3.6)
            self.vel_actual_2.setValue(dataframe_timestamp.velocity_ms_m1*3.6)
            largo = len(dataframe_global)
            #Asignar velocidad promedio 15 minutos
            # Idea: Resetear al salir del punto de control
            self.vel_cuarto_1.setValue(dataframe_global.velocity_ms_m1[largo-15*60:largo].mean()*3.6)
            self.vel_cuarto_2.setValue(dataframe_global.velocity_ms_m1[largo-15*60:largo].mean()*3.6)
            crono = dataframe_timestamp.index[0]-dataframe_global.head(1).index[0]
            self.tiempo_crono_1.setTime(QtCore.QTime(crono.components.hours,\
                                                     crono.components.minutes,\
                                                     crono.components.seconds))
            self.tiempo_crono_2.setTime(QtCore.QTime(crono.components.hours,\
                                                     crono.components.minutes,\
                                                     crono.components.seconds))
            self.curva1.setData(dataframe_global.velocity_ms_m1)
            self.curva1_1.setData(dataframe_global.velocity_ms_m2)
            self.curva4.setData(dataframe_global.velocity_ms_m1)
            self.curva4_1.setData(dataframe_global.velocity_ms_m2)
            #set SOC
            self.soc_1.setValue(dataframe_timestamp.soc_ah)
            self.soc_2.setValue(dataframe_timestamp.soc_ah)
            # N es el número de celda, y c es el numero de cmu
            self.voltaje_min_1.setText(str(round(dataframe_timestamp.minimum_cell_voltage.values[0]/1000,2))+' V C'\
                                       +str(int(dataframe_timestamp.cmu_number_minv.values[0]))+ ' N'\
                                       +str(int(dataframe_timestamp.cell_number_minv.values[0])))
            self.voltaje_min_2.setText(str(round(dataframe_timestamp.minimum_cell_voltage.values[0]/1000,2))+' V C'\
                                       +str(int(dataframe_timestamp.cmu_number_minv.values[0]))+ ' N'\
                                       +str(int(dataframe_timestamp.cell_number_minv.values[0])))
            self.voltaje_max_1.setText(str(round(dataframe_timestamp.maximum_cell_voltage.values[0]/1000,2))+' V C'\
                                       +str(int(dataframe_timestamp.cmu_number_maxv.values[0]))+ ' N'\
                                       +str(int(dataframe_timestamp.cell_number_maxv.values[0])))
            self.voltaje_max_2.setText(str(round(dataframe_timestamp.maximum_cell_voltage.values[0]/1000,2))+' V C'\
                                       +str(int(dataframe_timestamp.cmu_number_maxv.values[0]))+ ' N'\
                                       +str(int(dataframe_timestamp.cell_number_maxv.values[0])))
            #self.T_max_baterias_1.setValue(dataframe_global.cell_temperature_1.tail(1)/10)
            #print(dataframe_timestamp.maximum_cell_temp/10)
            self.t_max_1.setText(str(dataframe_timestamp.maximum_cell_temp.values[0]/10)+' °C cmu '\
                                 +str(int(dataframe_timestamp.cmu_number_maxt.values[0])))
            self.t_max_2.setText(str(dataframe_timestamp.maximum_cell_temp.values[0]/10)+' °C cmu '\
                                 +str(int(dataframe_timestamp.cmu_number_maxt.values[0])))
            # Mostrar valores detallados de motores
            self.vel1_1.setValue(dataframe_timestamp.velocity_ms_m1*3.6)
            self.vel2_1.setValue(dataframe_timestamp.velocity_ms_m2*3.6)
            self.vel1_2.setValue(dataframe_timestamp.velocity_ms_m1*3.6)
            self.vel2_2.setValue(dataframe_timestamp.velocity_ms_m2*3.6)

            if dataframe_timestamp.limit_flags_m1.values[0] == 1:
                self.limites_m1_1.setText('Voltaje Salida PWM')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 2:
                self.limites_m1_1.setText('Corriente Motor')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 4:
                self.limites_m1_1.setText('Velocidad')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 8:
                self.limites_m1_1.setText('Corriente BUS DC')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 16:
                self.limites_m1_1.setText('Voltaje BUS Max')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 32:
                self.limites_m1_1.setText('Voltaje BUS Min')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 64:
                self.limites_m1_1.setText('Temp. Motor')
            else:
                self.limites_m1_1.setText('---')

            if dataframe_timestamp.limit_flags_m1.values[0] == 1:
                self.limites_m1_2.setText('Voltaje Salida PWM')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 2:
                self.limites_m1_2.setText('Corriente Motor')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 4:
                self.limites_m1_2.setText('Velocidad')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 8:
                self.limites_m1_2.setText('Corriente BUS DC')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 16:
                self.limites_m1_2.setText('Voltaje BUS Max')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 32:
                self.limites_m1_2.setText('Voltaje BUS Min')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 64:
                self.limites_m1_2.setText('Temp. Motor')
            else:
                self.limites_m1_2.setText('---')

            if dataframe_timestamp.limit_flags_m2.values[0] == 1:
                self.limites_m2_1.setText('Voltaje Salida PWM')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 2:
                self.limites_m2_1.setText('Corriente Motor')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 4:
                self.limites_m2_1.setText('Velocidad')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 8:
                self.limites_m2_1.setText('Corriente BUS DC')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 16:
                self.limites_m2_1.setText('Voltaje BUS Max')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 32:
                self.limites_m2_1.setText('Voltaje BUS Min')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 64:
                self.limites_m2_1.setText('Temp. Motor')
            else:
                self.limites_m2_1.setText('---')\

            if dataframe_timestamp.limit_flags_m2.values[0] == 1:
                self.limites_m2_2.setText('Voltaje Salida PWM')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 2:
                self.limites_m2_2.setText('Corriente Motor')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 4:
                self.limites_m2_2.setText('Velocidad')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 8:
                self.limites_m2_2.setText('Corriente BUS DC')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 16:
                self.limites_m2_2.setText('Voltaje BUS Max')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 32:
                self.limites_m2_2.setText('Voltaje BUS Min')
            elif dataframe_timestamp.limit_flags_m1.values[0] == 64:
                self.limites_m2_2.setText('Temp. Motor')
            else:
                self.limites_m2_2.setText('---')



            # Errores
            if dataframe_timestamp.error_flags_m1.values[0] == 1:
                self.mot1_error_1.setText('---')
            elif dataframe_timestamp.error_flags_m1.values[0] == 2:
                self.mot1_error_1.setText('SW SobreCorriente')
            elif dataframe_timestamp.error_flags_m1.values[0] == 4:
                self.mot1_error_1.setText('DC BUS SobreVolt')
            elif dataframe_timestamp.error_flags_m1.values[0] == 8:
                self.mot1_error_1.setText('Secuencia Hall Mala')
            elif dataframe_timestamp.error_flags_m1.values[0] == 16:
                self.mot1_error_1.setText('Watchdog Reset')
            elif dataframe_timestamp.error_flags_m1.values[0] == 32:
                self.mot1_error_1.setText('CFG Error')
            elif dataframe_timestamp.error_flags_m1.values[0] == 64:
                self.mot1_error_1.setText('15V. UV')
            elif dataframe_timestamp.error_flags_m1.values[0] == 128:
                self.mot1_error_1.setText('IGBT Desaturación')
            elif dataframe_timestamp.error_flags_m1.values[0] == 256:
                self.mot1_error_1.setText('+15% vel lim mot')

            else:
                self.mot1_error_1.setText('---')

            if dataframe_timestamp.error_flags_m1.values[0] == 1:
                self.mot1_error_2.setText('---')
            elif dataframe_timestamp.error_flags_m1.values[0] == 2:
                self.mot1_error_2.setText('SW SobreCorriente')
            elif dataframe_timestamp.error_flags_m1.values[0] == 4:
                self.mot1_error_2.setText('DC BUS SobreVolt')
            elif dataframe_timestamp.error_flags_m1.values[0] == 8:
                self.mot1_error_2.setText('Secuencia Hall Mala')
            elif dataframe_timestamp.error_flags_m1.values[0] == 16:
                self.mot1_error_2.setText('Watchdog Reset')
            elif dataframe_timestamp.error_flags_m1.values[0] == 32:
                self.mot1_error_2.setText('CFG Error')
            elif dataframe_timestamp.error_flags_m1.values[0] == 64:
                self.mot1_error_2.setText('15V. UV')
            elif dataframe_timestamp.error_flags_m1.values[0] == 128:
                self.mot1_error_2.setText('IGBT Desaturación')
            elif dataframe_timestamp.error_flags_m1.values[0] == 256:
                self.mot1_error_2.setText('+15% vel lim mot')
            else:
                self.mot1_error_2.setText('---')

            if dataframe_timestamp.error_flags_m1.values[0] == 1:
                self.mot2_error_1.setText('---')
            elif dataframe_timestamp.error_flags_m1.values[0] == 2:
                self.mot2_error_1.setText('SW SobreCorriente')
            elif dataframe_timestamp.error_flags_m1.values[0] == 4:
                self.mot2_error_1.setText('DC BUS SobreVolt')
            elif dataframe_timestamp.error_flags_m1.values[0] == 8:
                self.mot2_error_1.setText('Secuencia Hall Mala')
            elif dataframe_timestamp.error_flags_m1.values[0] == 16:
                self.mot2_error_1.setText('Watchdog Reset')
            elif dataframe_timestamp.error_flags_m1.values[0] == 32:
                self.mot2_error_1.setText('CFG Error')
            elif dataframe_timestamp.error_flags_m1.values[0] == 64:
                self.mot2_error_1.setText('15V. UV')
            elif dataframe_timestamp.error_flags_m1.values[0] == 128:
                self.mot2_error_1.setText('IGBT Desaturación')
            elif dataframe_timestamp.error_flags_m1.values[0] == 256:
                self.mot2_error_1.setText('+15% vel lim mot')
            else:
                self.mot2_error_1.setText('---')

            if dataframe_timestamp.error_flags_m1.values[0] == 1:
                self.mot2_error_2.setText('---')
            elif dataframe_timestamp.error_flags_m1.values[0] == 2:
                self.mot2_error2.setText('SW SobreCorriente')
            elif dataframe_timestamp.error_flags_m1.values[0] == 4:
                self.mot2_error2.setText('DC BUS SobreVolt')
            elif dataframe_timestamp.error_flags_m1.values[0] == 8:
                self.mot2_error2.setText('Secuencia Hall Mala')
            elif dataframe_timestamp.error_flags_m1.values[0] == 16:
                self.mot2_error2.setText('Watchdog Reset')
            elif dataframe_timestamp.error_flags_m1.values[0] == 32:
                self.mot2_error2.setText('CFG Error')
            elif dataframe_timestamp.error_flags_m1.values[0] == 64:
                self.mot2_error2.setText('15V. UV')
            elif dataframe_timestamp.error_flags_m1.values[0] == 128:
                self.mot2_error2.setText('IGBT Desaturación')
            elif dataframe_timestamp.error_flags_m1.values[0] == 256:
                self.mot2_error2.setText('+15% vel lim mot')
            else:
                self.mot2_error2.setText('---')


    @QtCore.pyqtSlot(dict)
    def recibir_data_serial(self, data):
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
            data_salida = dict(data='THREAD SERIAL', hora=datetime.datetime.now())
            self.serial_signal.emit(data_salida)
            #time.sleep(1)


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
        self.multicast_group = '239.255.60.60'
        self.server_address = ('', 4876)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.server_address)
        self.group = socket.inet_aton(self.multicast_group)
        self.mreq = struct.pack('4sL', self.group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, self.mreq)
        while self.alive:
            data, address = self.sock.recvfrom(1024)
            data_salida = dict(data=data, direccion=address)
            self.udp_signal.emit(data_salida)
            #time.sleep(1)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
