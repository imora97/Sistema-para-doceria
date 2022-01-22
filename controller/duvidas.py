from qt_core import*

class Duvidas(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/duvidas.ui', self)
        