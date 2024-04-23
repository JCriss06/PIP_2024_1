#aqui van todos los programas que deben conectarse al principal
import sys
from PyQt5 import QtWidgets
import Ejercicios as interfaz

import E8_Ejecutable
import E9_Ejecutable

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_ejercicio8.clicked.connect(self.ejercicio8)
        self.btn_ejercicio9.clicked.connect(self.ejercicio9)
    # Área de los Slots
    def ejercicio8(self):
        self.dialogo = E8_Ejecutable.MyDialog()
        self.dialogo.setModal(False)
        self.dialogo.show()

    def ejercicio9(self):
        self.dialogo = E9_Ejecutable.MyDialog()
        self.dialogo.setModal(False)
        self.dialogo.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())