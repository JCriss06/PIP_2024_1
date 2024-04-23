import sys
from PyQt5 import uic, QtWidgets, QtCore
from pygame import mixer
qtCreatorFile = "RelojConAlarma.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.alarma_sonada = False # controla si la alarma ya sono

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.obtener_tiempo)
        self.segundoPlano.start(1000)

        self.cb_horas.addItems(str(h) for h in range(24))
        self.cb_minutos.addItems(str(m) for m in range(60))
        #self.cb_segundos.addItems(str(s) for s in range(60))
        self.cb_repetir.addItems(str(r) for r in range(1, 5))

        self.btn_configurar.clicked.connect(self.configurar_alarma)

    # Área de los Slots
    def obtener_tiempo(self):
        self.tiempo_actual = QtCore.QTime.currentTime()
        self.hora_actual = self.tiempo_actual.toString('hh')
        self.minutos_actual = self.tiempo_actual.toString('mm')
        self.segundos_actual = self.tiempo_actual.toString('ss')

        self.x_hora = self.cb_horas.currentText()
        self.x_minutos = self.cb_minutos.currentText()
        #self.x_segundos = self.cb_segundos.currentText()

        self.lcd_actual.display(f"{self.hora_actual}:{self.minutos_actual}:{self.segundos_actual}")
        self.lcd_alarma.display(f"{self.x_hora}:{self.x_minutos}")#:{self.x_segundos}

        if not self.alarma_sonada and int(self.hora_actual) == int(self.x_hora) and int(self.minutos_actual) == int(self.x_minutos) : #and int(self.segundos_actual) == int(self.x_segundos)
            mixer.init()
            mixer.music.load("Music Box.mp3")
            mixer.music.play(loops=int(self.cb_repetir.currentText()))

            self.msj = QtWidgets.QMessageBox()
            self.msj.setText("Wake up!")
            self.msj.setWindowTitle("Alarma")
            self.msj.exec_()

            self.alarma_sonada = True

    def configurar_alarma(self): # resetea la bandera cuando se configura una nueva alarma
        self.alarma_sonada = False
        self.confi = QtWidgets.QMessageBox()
        self.confi.setText("Se configuro una nueva alarma!")
        self.confi.setWindowTitle("Nueva Alarma")
        self.confi.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())