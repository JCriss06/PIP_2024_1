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
        self.dialog_mascotas = {  # ejemplos para el equipo
            1: ['hamster', 'comer', 5, 'a+', ''],
            2: ['gato', 'correr', 8, 'b+', ''],
            3: ['cuyo', 'jugar', 9, 'c+', ''],
            4: ['perro', 'ladrar', 1, 'd+', ''],
            5: ['conejo', 'saltar', 5, 'e+', ''],
        }
        self.dialog_mascotas.setMaxpyimum = 1
        self.dialog_mascotas.setMinimum = 1
        self.dialog_mascotas.setsingleStop = 1
        self.dialog_mascotas.value = 1
        self.dialog_mascotas.currentValueChange.connect(self.cambio)




    # Área de los Slots
    def cambio(self):
        print('Text: '+self.cambio_mascotas.currentIndex())
        print('Text: ' + str(self.cambio_mascotas.currentIndex()))
        print('Text: ' + str(self.cambio_mascotas.currentIndex()))

        dataClave = self.cambio_mascotas.currentIndex()
        imagen = self.datos_mascotas[dataClave][-1]
        self.ima_persona.setPixmap



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