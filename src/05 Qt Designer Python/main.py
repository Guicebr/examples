from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("src\\05 Qt Designer Python\dialog.ui")


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()