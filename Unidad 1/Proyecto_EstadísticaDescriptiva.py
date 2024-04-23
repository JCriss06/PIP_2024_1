import sys
import numpy as np
from scipy import stats as st
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Proyecto_EstadísticaDescriptiva.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_moda.clicked.connect(self.operacion)
        self.btn_mediana.clicked.connect(self.operacion)
        self.btn_promedio.clicked.connect(self.operacion)
        self.btn_desvestandar.clicked.connect(self.operacion)
        self.btn_valormayor.clicked.connect(self.operacion)
        self.btn_valormenor.clicked.connect(self.operacion)
        self.btn_varianza.clicked.connect(self.operacion)
        self.txt_resultado.setReadOnly(True)

    # Área de los Slots
    def operacion(self):
        try:
            objeto = self.sender()
            nombre = objeto.objectName()

            lista_str = self.txt_numeros.text()
            lista_en_numeros = [float(i) for i in lista_str.split(",")]

            if nombre == "btn_moda":
                resultado = st.mode(lista_en_numeros)[0]
                self.txt_resultado.setText(str(resultado))
            elif nombre == "btn_mediana":
                resultado = np.median(lista_en_numeros)
                self.txt_resultado.setText(str(resultado))
            elif nombre == "btn_promedio":
                resultado = np.average(lista_en_numeros)
                self.txt_resultado.setText(str(resultado))
            elif nombre == "btn_desvestandar":
                resultado = np.std(lista_en_numeros)
                self.txt_resultado.setText(str(resultado))
            elif nombre == "btn_valormayor":
                resultado = np.max(lista_en_numeros)
                self.txt_resultado.setText(str(resultado))
            elif nombre == "btn_valormenor":
                resultado = np.min(lista_en_numeros)
                self.txt_resultado.setText(str(resultado))
            elif nombre == "btn_varianza":
                resultado = np.var(lista_en_numeros)
                self.txt_resultado.setText(str(resultado))

            # Redondear el resultado a 4 decimales
            if nombre == "btn_moda":
                self.txt_resultado.setText(str(resultado))
            else:
                resultado_redondeado = round(resultado, 4)
                self.txt_resultado.setText(str(resultado_redondeado))

        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())