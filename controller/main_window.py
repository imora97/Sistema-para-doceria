from controller.login import Login
from qt_core import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        # página inicial
        #self.stackedWidget.insertWidget(0, Login())

        # ações botões
        self.enter.clicked.connect(self.fazlogin)

    def fazlogin(self):
        self.stackedWidget.insertWidget(0, Login())
        self.stackedWidget.setCurrentIndex(0)