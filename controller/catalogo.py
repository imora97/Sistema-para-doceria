from qt_core import*

class CatalogoDoces(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/catalogo.ui', self)
    