from controller.cad_clientes import CadCliente
import model.doces_dao as doces_dao
from qt_core import *


class CadDoce(QWidget):

    def __init__(self, janela_doces):
        super().__init__()
        uic.loadUi('view/cadastrodoces.ui', self)

        self.janela_doces = janela_doces     #### essa janela tem utilidade??

        # lista
        self.lista_doces = None

        self.finalizar.clicked.connect(self.salvar_doce)
        self.cancelar.clicked.connect(self.cancelar_doce)
        self.cad_c.clicked.connect(self.abre_cad_cliente)


    def salvar_doce(self):
        if self.nome.text() == '' or self.peso.text() == '' or self.valor.text() == '':
            print('Dados obrigatórios *')

        # atualiza tabela
        self.janela_doces.carrega_dados()        
        
        self.close()

    def carrega_dados(self):
        cadlista = doces_dao.lista_doces
        self.tabela.setRowCount(0)
        for db in cadlista:
            self.add_linha(db)

    def add_linha(self, db):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

    def abre_cad_cliente(self):
        self.cliente_window = CadCliente(self)
        self.cliente_window.show()

    def cancelar_doce(self):
        self.close()
