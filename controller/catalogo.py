from controller.beijinho import beijinho
from controller.brigadeiro import brigadeiro
from qt_core import*

class CatalogoDoces(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/catalogo.ui', self)

        # bottons
        self.brigadeiro.clicked.connect(self.brigadeiro)
        self.beijinho.clicked.connect(self.beijinho)


    def brigadeiro(self):
        self.painel_pricipal.insertWidget(brigadeiro())
        self.gridLayout.setCurrentIndex()

    def beijinho(self):
        self.gridLayout.insertWidget(beijinho())
        self.gridLayout.setCurrentIndex()


        