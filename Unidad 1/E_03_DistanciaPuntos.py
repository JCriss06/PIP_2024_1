import math
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_03_DistanciaPuntos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        x1 = float(self.txt_x1.text())
        x2 = float(self.txt_x2.text())
        y1 = float(self.txt_y1.text())
        y2 = float(self.txt_y2.text())
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        self.label_resultado.setText(f'Resultado = {round(distancia, 4)}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



