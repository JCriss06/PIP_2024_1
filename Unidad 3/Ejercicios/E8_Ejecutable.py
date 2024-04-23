import sys
import E8_Vinicultores as interfaz

from PyQt5 import uic, QtWidgets, QtGui

class MyDialog(QtWidgets.QDialog, interfaz.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        interfaz.Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_tipo.addItem("Selecciona...", 0)
        self.cb_tipo.addItem("A", 1)
        self.cb_tipo.addItem("B", 2)
        self.cb_tamano.addItem("Selecciona...", 0)
        self.cb_tamano.addItem("1", 1)
        self.cb_tamano.addItem("2", 2)
        self.txt_final.setEnabled(False)

        self.btn_calcular.clicked.connect(self.venta)

    # Área de los Slots
    def venta(self):
        inicial = float(self.txt_inicial.text())
        self.x_tipo = self.cb_tipo.currentText()
        self.x_tamano = self.cb_tamano.currentText()

        if (self.x_tipo == "A" and self.x_tamano == "1"):
            inicial = inicial + 20
            self.txt_final.setText(str(inicial))
        if(self.x_tipo == "A" and self.x_tamano == "2"):
            inicial = inicial + 30
            self.txt_final.setText(str(inicial))
        if(self.x_tipo == "B" and self.x_tamano == "1"):
            inicial  = inicial - 30
            self.txt_final.setText(str(inicial))
        if(self.x_tipo == "B" and self.x_tamano == "2"):
            inicial = inicial - 50
            self.txt_final.setText(str(inicial))