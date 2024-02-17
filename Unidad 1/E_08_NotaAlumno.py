import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_08_NotaAlumno.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_saludar.clicked.connect(self.CalcularNotas)
    # Área de los Slots
    def CalcularNotas(self):
        # pass

        msj = QtWidgets.QMessageBox()
        msj.setText(self.Notas())
        msj.exec_()

    def Notas(self):
        numero = int(self.txt_numCalf.text())
        if numero == 10:
            return "Tu nota es A"
        elif numero == 9:
            return "Tu nota es B"
        elif numero == 8:
            return "Tu nota es C"
        elif numero == 7:
            return "Tu nota es D"
        elif numero == 6:
            return "Tu nota es E"
        else:
            return "Tu nota es F"



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

