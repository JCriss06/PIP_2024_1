import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P18_InterfazConexionArduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.txt_temperatura.setEnabled(False)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)

    #Area de Slots
    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "Conectar" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
            self.btn_accion.setText("Desconectar")
            self.txt_estado.setText("Conectado")
        elif texto_boton == "Desconectar" and self.arduino.isOpen():
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("Reconectar")
            self.txt_estado.setText("Desconectado")
        else:
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_accion.setText("Desconectar")
            self.txt_estado.setText("Conectado")

    def lecturaArduino(self): #probar
        if not self.arduino is None:
            if self.arduino.inWaiting() :
                cadena = self.arduino.readline()
                cadena = cadena.decode()
                cadena = cadena.strip()
                if cadena != "":
                    self.txt_temperatura.setText(cadena)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())