from qt_core import*

class beijinho(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/beijinho.ui', self)
        