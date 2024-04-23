import sys
import E9_ViajeDeEstudios as interfaz
from PyQt5 import uic, QtWidgets, QtGui


class MyDialog(QtWidgets.QDialog, interfaz.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        interfaz.Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular)
        self.txt_cobrar.setEnabled(False)
        self.txt_pagar.setEnabled(False)

    # Área de los Slots
    def calcular(self):
        asistentes = int(self.txt_asistentes.text())

        if(asistentes >= 100 ):
            cobro = 65
            costo = cobro * asistentes
            self.txt_cobrar.setText(str(cobro))
            self.txt_pagar.setText(str(costo))
        if(asistentes >= 50 and asistentes <= 99):
            cobro = 70
            costo = cobro * asistentes
            self.txt_cobrar.setText(str(cobro))
            self.txt_pagar.setText(str(costo))
        if(asistentes >= 30 and asistentes <= 49):
            cobro = 95
            costo = cobro * asistentes
            self.txt_cobrar.setText(str(cobro))
            self.txt_pagar.setText(str(costo))
        if(asistentes < 30):
            cobro = "-"
            costo = 4000
            self.txt_cobrar.setText(cobro)
            self.txt_pagar.setText(str(costo))