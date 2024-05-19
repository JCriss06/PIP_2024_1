import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P21_InterfazConexionArduino1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None

    #Area de Slots
    def accion(self):
        texto_boton = self.btn_accion.text() #CONECTAR
        com = self.txt_com.text() #
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO") #agregar
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
        else:
            self.arduino.open()
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())