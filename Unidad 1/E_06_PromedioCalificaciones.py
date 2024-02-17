import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_06_PromedioCalificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.promedioCalificaciones)
        self.txt_resultado.setEnabled(False)
    # Área de los Slots
    def promedioCalificaciones(self):
        calif1 = float(self.txt_calif1.text())
        calif2 = float(self.txt_calif2.text())
        calif3 = float(self.txt_calif3.text())
        calif4 = float(self.txt_calif4.text())
        calif5 = float(self.txt_calif5.text())
        promedio = (calif1 + calif2 + calif3 + calif4 + calif5) / 5
        self.txt_resultado.setText(str(promedio))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())