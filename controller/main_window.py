from controller.catalogo import CatalogoDoces
from controller.duvidas import Duvidas
from controller.observacao import Obs
from controller.zap import ChamaZap
from qt_core import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        # página inicial
       # self.stackedWidget.insertWidget(0, Inicio())

        # ações botões
        #self.botaologo.clicked.connect(self.Inicio)
        self.catalog.clicked.connect(self.CatalogoDoces)
        self.duvida.clicked.connect(self.Duvidas)
        self.obs.clicked.connect(self.Obs)
        self.zap.clicked.connect(self.ChamaZap)

    #def Inicio(self):
     #   self.stackedWidget.insertWidget(0, Inicio())
      #  self.stackedWidget.setCurrentIndex(0)
        
    def CatalogoDoces(self):
        self.stackedWidget.insertWidget(0, CatalogoDoces())
        self.stackedWidget.setCurrentIndex(0)

    def Duvidas(self):
        self.stackedWidget.insertWidget(0, Duvidas())
        self.stackedWidget.setCurrentIndex(0)

    def Obs(self):
        self.stackedWidget.insertWidget(0, Obs())
        self.stackedWidget.setCurrentIndex(0)

    def ChamaZap(self):
        self.stackedWidget.insertWidget(0, ChamaZap())
        self.stackedWidget.setCurrentIndex(0)