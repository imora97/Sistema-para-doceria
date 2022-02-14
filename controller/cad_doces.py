from controller.cad_vendas import CadVenda
import model.doces_dao as doces_dao
from qt_core import *


class CadDoce(QWidget):

    def __init__(self, janela_doces):
        super().__init__()
        uic.loadUi('view/cadastrodoces.ui', self)

        self.janela_doces = janela_doces
        self.doce_atual = None

        # lista
        self.lista_doces = None

        self.salvar.clicked.connect(self.salvar_doce)
        self.cancelar.clicked.connect(self.cancelar_doce)
        self.cad_v.clicked.connect(self.abre_cad_venda)
        self.limpa.clicked.connect(self.limpar)
        self.excluir_button.clicked.connect(self.excluir)

    def salvar_doce(self):
        if self.nome.text() == '' or self.peso.text() == '' or self.valor.text() == '' or self.tipo.currentText() == '':
            print('\033[7;35;44mDados obrigatórios *\033[m')

            return None
        # atualiza tabela
        #self.janela_doces.carrega_dados()
        self.close()

    def carrega_dados(self):
        self.cadlista = doces_dao.selectAll()
        self.limpa()
        self.tabela.setRowCount(0)
        for db in self.cadlista:
            self.add_linha(db)

    def add_linha(self, db):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        id = QTableWidgetItem(str(db.id))
        nome = QTableWidgetItem(db.nome)
        peso = QTableWidgetItem(db.peso)
        tipo = QTableWidgetItem(db.tipo)
        valor = QTableWidgetItem(db.valor)

        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, peso)
        self.tabela.setItem(rowCount, 3, tipo)
        self.tabela.setItem(rowCount, 4, valor)

    def cancelar_doce(self):
        self.close()

    def excluir(self):
        if self.doce_atual != None:
            doces_dao.delete(self.doce_atual.id)
            self.carrega_dados()

            ##### COLOCAR COMANDO DE CAIXA DE SELEÇÃO

    def limpar(self):
        self.nome.clear()
        self.peso.clear()
        self.tipo.clear()
        self.valor.clear()

    def abre_cad_venda(self):
        self.venda_window = CadVenda(self)
        self.venda_window.show()