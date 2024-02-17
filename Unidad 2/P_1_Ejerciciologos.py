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
        self.datos_mascotas ={#ejemplos para el equipo
            1:['hamster', 'comer', 5,'a+',''],
            2:['gato', 'correr', 8, 'b+',''],
            3: ['cuyo', 'jugar', 9, 'c+',''],
            4: ['perro', 'ladrar', 1, 'd+',''],
            5: ['conejo', 'saltar', 5, 'e+',''],
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)
        self.index_control = 0

    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_mascotas(self.index_control)
            print(datos)
            self.btn_adelante.setEnable(True)
            #cambiar foto
            self.img_persona

        #if self.index_control


    def adelante(self):
        self.index_control += 1



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())