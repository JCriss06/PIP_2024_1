import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P_1_Ejerciciologos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_gato.toggled.connect(self.sel_gato)
        self.cb_cuyo.toggled.connect(self.sel_cuyo)
        self.cb_perro.toggled.connect(self.sel_perro)
        self.cb_conejo.toggled.connect(self.sel_conejo)

        self.gato = ''
        self.cuyo = ''
        self.perro = ''
        self.conejo = ''

    # Área de los Slots
    def sel_gato(self):
        if self.cb_gato.isChecked():
            print("Gato True")
            self.gato = 'Gato'
        else:
            print("Gato False")
            self.gato = ""
            self.text_equipo.setPlanText(self.gato+self.cuyo+self.perro+self.conejo)

    def sel_cuyo(self):
        if self.cb_cuyo.isChecked():
            print("Cuyo True")
            self.cuyo = 'Cuyo'
        else:
            print("Cuyo False")
            self.cuyo = ""
            self.text_equipo.setPlanText(self.gato+self.cuyo+self.perro+self.conejo)

    def sel_perro(self):
        if self.cb_perro.isChecked():
            print("Perro True")
            self.perro = 'Perro'
        else:
            print("Perro False")
            self.perro = ""
            self.text_equipo.setPlanText(self.gato+self.cuyo+self.perro+self.conejo)
    def sel_conejo(self):
        if self.cb_conejo.isChecked():
            print("Conejo True")
            self.conejo = 'Conejo'
        else:
            print("Conejo False")
            self.conejo = ""
            self.text_equipo.setPlanText(self.gato+self.cuyo+self.perro+self.conejo)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())