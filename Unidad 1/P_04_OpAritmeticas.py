import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpAritmeticas_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_restar.clicked.connect(self.restar)
        self.btn_multiplicar.clicked.connect(self.multiplicacion)
        self.btn_dividir.clicked.connect(self.division)
        self.txt_resultado.setEnabled (False)

    # Área de los Slots
    def sumar(self):
        A = int(self.txt_a.text())
        B = int(self.txt_b.text())
        r = A + B
        self.txt_resultado.setText(str(r))

    def restar(self):
        A = int(self.txt_a.text())
        B = int(self.txt_b.text())
        r = A - B
        self.txt_resultado.setText(str(r))

    def multiplicacion(self):
        A = int(self.txt_a.text())
        B = int(self.txt_b.text())
        r = A * B
        self.txt_resultado.setText(str(r))

    def division(self):
        A = int(self.txt_a.text())
        B = int(self.txt_b.text())
        r = A / B
        self.txt_resultado.setText(str(r))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())