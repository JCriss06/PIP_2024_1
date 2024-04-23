import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_equipo = {
            1: ["Alfonso Aldama", "GYM", 20, "a+", ":/integrantes/Imagenes/poncho.jpg"],
            2: ["Adan Clemente", "Ir al super", 20, "b+", ":/integrantes/Imagenes/adan.jpg"],
            3: ["Jesus Cristobal", "Dormir", 20, "c+", ":/integrantes/Imagenes/cristobal.jpg"],
            4: ["Pavel Dominguez", "Jugar", 20, "d+", ":/integrantes/Imagenes/pavel.jpg"]
        }

        self.combo_equipo.addItem("Selecciona...", 0)
        self.combo_equipo.addItem("Alfonso Aldama", 1)
        self.combo_equipo.addItem("Adan Clemente", 2)
        self.combo_equipo.addItem("Jesus Cristobal", 3)
        self.combo_equipo.addItem("Pavel Dominguez", 4)

        self.combo_equipo.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text: " + self.combo_equipo.currentText())
        print("Index: " + str(self.combo_equipo.currentIndex()))
        print("Data: " + str(self.combo_equipo.currentData()))

        dataClave = self.combo_equipo.currentData()
        imagen = self.datos_equipo[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())