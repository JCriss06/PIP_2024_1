import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P1_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_equipo = {
            1: ["Alfonso Aldama", "GYM", 20, "a+", ":/integrantes/Imagenes/poncho.jpg"],
            2: ["Adan Clemente", "Ir al super" ,20, "b+", ":/integrantes/Imagenes/adan.jpg"],
            3: ["Jesus Cristobal", "Dormir", 20, "c+", ":/integrantes/Imagenes/cristobal.jpg"],
            4: ["Pavel Dominguez", "Jugar", 20, "d+", ":/integrantes/Imagenes/pavel.jpg"]
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.index_control = 0
        self.btn_atras.setEnabled(False)

    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_equipo[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            #change img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
            self.txt_nombre.setText(datos[-5])
        if self.index_control == 1:
            self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control < 4:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_equipo[self.index_control]
            print(datos)
            #change img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 4:
            self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())