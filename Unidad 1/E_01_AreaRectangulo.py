import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_01_AreaRectangulo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcularArea)

    # Área de los Slots
    def calcularArea(self):
        base = float(self.txt_base.text())
        altura = float(self.txt_altura.text())

        area = base * altura
        cadena = "El área del rectángulo es: " + str(area)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())