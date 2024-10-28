from PyQt6.QtWidgets import *

# Creamos la Aplicacion
app = QApplication([])

# Definimos el boton
button = QPushButton('Click')

# Funcion que se ejecutara al presionar el boton
# Muestra un texto por pantalla
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

# Seteamos un listener en el boton, para observar cuando es clickado y le asignamos la funcion
button.clicked.connect(on_button_clicked)
button.show()
app.exec()
