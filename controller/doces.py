from controller.cadastro import Cadastro
import model.doces_dao as doces_dao
from qt_core import*


class DocesPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/doces.ui', self)

        self.doce_window = None
        self.carrega_dados()

        #botão novo doce
        self.novo_doce.clicked.connect(self.novo_doce)

    def novo_doce(self):
        # cria a janela de cadastro
        self.doce_window = Cadastro(self)
        self.doce_window.show()

    def carrega_dados(self):
        lista = doces_dao.lista_doces
        self.tabela.setRowCount(0)
        for c in lista:
            self.add_linha(c)

    def add_linha(self, c):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)
