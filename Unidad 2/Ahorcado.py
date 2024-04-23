import sys
from PyQt5 import uic, QtWidgets
import random
qtCreatorFile = "Ahorcado.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_newpalabra.clicked.connect(self.nuevaPalabra)
        self.btn_comprobar.clicked.connect(self.comprobar)
        self.txt_secreta.setEnabled(False)

        self.reiniciar_juego = False
        self.secreta = ""
        self.cadena = ""
        self.intentos = 0

    # Área de los Slots
    def nuevaPalabra(self):
        if self.reiniciar_juego:
            self.reiniciar_juego = False
        else:
            palabras = ['python', 'programacion', 'elefante', 'conocimiento', 'paralelepipedo',
                        'escarabajo', 'spotify', 'crucigrama', 'twitch', 'exotico',
                        'estallido', 'vaquero', 'orquidea', 'legumbre', 'quimica',
                        'invierno', 'espectro', 'paraguas', 'calabaza', 'escarabajo',
                        'orangutan', 'espectro', 'extraordinario', 'desafio', 'misterio']
            self.secreta = random.choice(palabras)
            self.cadena = "-" * len(self.secreta)
            self.intentos = 0
            self.txt_secreta.setText(self.cadena)
            self.txt_dibujo.clear()
            self.txt_letra.clear()
    def comprobar(self):
        if self.reiniciar_juego:
            return

        self.letra = self.txt_letra.text()
        if self.letra in self.secreta:
            for i in range(len(self.secreta)):
                if self.secreta[i] == self.letra:
                     self.cadena = self.cadena[:i] + self.letra + self.cadena[i+1:]
                     self.txt_secreta.setText(self.cadena)
        else:
            self.intentos += 1
            if self.intentos == 1:
                self.txt_dibujo.setPlainText("O")
            elif self.intentos == 2:
                self.txt_dibujo.setPlainText(" O\n" + "/\n")
            elif self.intentos == 3:
                self.txt_dibujo.setPlainText(" O\n" + "/|\n")
            elif self.intentos == 4:
                self.txt_dibujo.setPlainText(" O\n" + "/|\\\n")
            elif self.intentos == 5:
                self.txt_dibujo.setPlainText(" O\n" + "/|\\\n" + " |\n")
            elif self.intentos == 6:
                self.txt_dibujo.setPlainText(" O\n" + "/|\\\n" + " |\n" + "/\n")
            elif self.intentos == 7:
                self.txt_dibujo.setPlainText(" O\n" + "/|\\\n" + " |\n" + "/ \\")
                loser = QtWidgets.QMessageBox()
                loser.setText(f'!Has perdido el juego¡. La palabra secreta era: {self.secreta}')
                loser.exec_()
                self.reiniciar_juego = True

        if self.cadena == self.secreta:
            winner = QtWidgets.QMessageBox()
            winner.setText(f'!Felicidades ganaste¡. La palabra secreta era: {self.secreta}')
            winner.exec_()
            self.reiniciar_juego = True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())