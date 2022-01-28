from model.doces import Doces
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

    def abre_cad_doce(self):
        # abre a janela de cadastro
        self.doce_window = CadDoce(self)
        self.doce_window.show()

    def carrega_dados(self):
        lista = doces_dao.lista_doces
        self.tabela.setRowCount(0)
        for l in lista:
            self.add_linha(l)

    def add_linha(self, l):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        #_____________________________________CONCLUIR
    """id = (str(l.id))
        nome = (str(l.nome))
        peso = (str(l.peso))
        tipo = (str(l.tipo))
        valor = (str(l.valor))"""

        # insere elementos a tabela na coluna correspondente (linha, coluna, item)
        #_____________________________________CONCLUIR
    """self.tabela.setItem(rowCount, 0, id)"""