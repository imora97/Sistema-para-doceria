from controller.catalogo import CatalogoDoces
from controller.duvidas import Duvidas
from controller.observacao import Obs
from controller.zap import ChamaZap
from qt_core import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)


        # ações botões
        self.catalog.clicked.connect(self.CatalogoDoces)
        self.duvida.clicked.connect(self.Duvidas)
        self.obs.clicked.connect(self.Obs)
        self.zap.clicked.connect(self.ChamaZap)


    def CatalogoDoces(self):
        self.stackedWidget.insertWidget(0, CatalogoDoces())
        self.painel_principal.setCurrentIndex(0)

    def Duvidas(self):
        self.stackedWidget.insertWidget(0, Duvidas())
        self.painel_principal.setCurrentIndex(0)

    def Obs(self):
        self.stackedWidget.insertWidget(0, Obs())
        self.painel_principal.setCurrentIndex(0)

    def ChamaZap(self):
        self.stackedWidget.insertWidget(0, ChamaZap())
        self.painel_principal.setCurrentIndex(0)