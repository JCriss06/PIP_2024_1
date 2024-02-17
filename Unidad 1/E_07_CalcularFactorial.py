import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_07_CalcularFactorial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_saludar.clicked.connect(self.CalcularFactorial)
    # Área de los Slots
    def CalcularFactorial(self):
        # pass
        numero = int(self.txt_numfactorial.text())
        resultado = self.factorial(numero)
        msj = QtWidgets.QMessageBox()
        msj.setText(str(resultado))
        msj.exec_()

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

