import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P13_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_aldama.clicked.connect(self.click_aldama)
        self.rb_aldama.toggled.connect(self.toggle_aldama)

    # Área de los Slots
    def click_aldama(self):
        print('hiciste click a aldama ')

    def toggle_aldama(self):
        estado = self.rb_aldama.isChecked()
        print('aldama cambio de estado (toggle)')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())