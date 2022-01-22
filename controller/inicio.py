from qt_core import*

class Inicio(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/inicio.ui', self)