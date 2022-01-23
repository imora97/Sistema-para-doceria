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
        """self.bolo_p.clicked.connect(self.bolop)
        self.bolo_m.clicked.connect(self.bolom)
        self.bolo_g.clicked.connect(self.bolog)"""




    def brigadeiro(self):
        self.gridLayout.setCurrentIndex()

    def beijinho(self):
        self.gridLayout.setCurrentIndex()

    """def bolop(self):
        self.gridLayout.insertWidget(0, bolop())
        self.bolop.setCurrentIndex(0)

    def bolom(self):
        self.gridLayout.insertWidget(0, bolom())
        self.bolom.setCurrentIndex(0)

    def bolog(self):
        self.gridLayout.insertWidget(0, bolog())
        self.bolog.setCurrentIndex(0)"""
        