import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VerticalSlider.ui"  # Nombre del archivo aquí.
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

        self.vs_equipo.setMinimum(1)
        self.vs_equipo.setMaximum(4)
        self.vs_equipo.setSingleStep(1)
        self.vs_equipo.setValue(1)
        self.vs_equipo.valueChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        dataClave = self.vs_equipo.value()
        print(dataClave)
        imagen = self.datos_equipo[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())