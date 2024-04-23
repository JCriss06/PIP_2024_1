import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_aldama.toggled.connect(self.sel_aldama)
        self.cb_clemente.toggled.connect(self.sel_clemente)
        self.cb_cristobal.toggled.connect(self.sel_cristobal)
        self.cb_pavel.toggled.connect(self.sel_pavel)

        self.aldama = ""
        self.clemente = ""
        self.cristobal = ""
        self.pavel = ""

    # Área de los Slots
    def sel_aldama(self):
        if self.cb_aldama.isChecked():
            print("Aldama True")
            self.aldama = "ALDAMA\n"
        else:
            print("Aldama False")
            self.aldama = ""
        self.txt_equipo.setPlainText(self.aldama + self.clemente + self.cristobal + self.pavel)
    def sel_clemente(self):
        if self.cb_clemente.isChecked():
            print("Clemente True")
            self.clemente = "CLEMENTE\n"
        else:
            print("Clemente False")
            self.clemente = ""
        self.txt_equipo.setPlainText(self.aldama + self.clemente + self.cristobal + self.pavel)
    def sel_cristobal(self):
        if self.cb_cristobal.isChecked():
            print("Cristobal True")
            self.cristobal = "CRISTOBAL\n"
        else:
            print("Cristobal False")
            self.cristobal = ""
        self.txt_equipo.setPlainText(self.aldama + self.clemente + self.cristobal + self.pavel)
    def sel_pavel(self):
        if self.cb_pavel.isChecked():
            print("Pavel True")
            self.pavel = "PAVEL\n"
        else:
            print("Pavel False")
            self.pavel = ""
        self.txt_equipo.setPlainText(self.aldama + self.clemente + self.cristobal + self.pavel)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())