from qt_core import*
import model.doces_dao as doces_dao
from controller.cad_doces import CadDoce


class CatalogoDoces(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/catalogo.ui', self)
    
        self.carrega_dados()

        self.cad_db.clicked.connect(self.abre_cad_doce)

        # configuração tabela - 
        """CONCLUIR"""

    def carrega_dados(self):
        self.lista = doces_dao.selectAll()
        self.tabela.setRowCount(0)
        for l in self.lista:
            self.add_linha(l)

    def add_linha(self, l):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        #____ ??*
        id = QTableWidgetItem(str(l.id))
        nome = QTableWidgetItem(str(l.nome))
        peso = QTableWidgetItem(str(l.peso))
        tipo = QTableWidgetItem(str(l.tipo))
        valor = QTableWidgetItem(str(l.valor))

        # insere elementos a tabela (linha, coluna, item)
        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, peso)
        self.tabela.setItem(rowCount, 3, tipo)
        self.tabela.setItem(rowCount, 4, valor)

    def abre_cad_doce(self):
        # abre a janela de cadastro
        self.doce_window = CadDoce(self)
        self.doce_window.show()