from controller.cad_vendas import CadVenda
from qt_core import *
import model.clientes_dao as clientes_dao


class CadCliente(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/cadastroclientes.ui', self)

        # lista
        self.lista_clientes = None

        self.carrega_dados()

        self.finalizar.clicked.connect(self.salvar_cliente)
        self.cancelar.clicked.connect(self.cancelar_cliente)
        self.cad_v.clicked.connect(self.abre_cad_venda)

    
    def salvar_cliente(self):
        if self.nome.text() == '' or self.telefone.text() == '':
            print('Dados obrigatórios *')

        self.close()
        
    def carrega_dados(self):
        cc = clientes_dao.lista_clientes
        self.tabela.setRowCount(0)
        for cadc in cc:
            self.add_linha(cadc)

    def add_linha(self, cadc):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

    def abre_cad_venda(self):
        self.venda_window = CadVenda(self)
        self.venda_window.show()

    def cancelar_cliente(self):
        self.close()