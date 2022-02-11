from qt_core import *
import model.clientes_dao as clientes_dao


class CadCliente(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/cadastroclientes.ui', self)

        # insere tabela no layout
        #self.table = TabelaCliente(self)

        # lista
        self.lista_clientes = None

        self.finalizar.clicked.connect(self.salvar_cliente)
        self.cancelar.clicked.connect(self.cancelar_cliente)
        self.limpar.clicked.connect(self.limpa)
    
    def salvar_cliente(self):
        if self.nome.text() == '' or self.telefone.text() == '':
            print('Dados obrigatórios *')

            return None
            
        self.close()
        
    def carrega_dados(self):
        self.cc = clientes_dao.selectAll()
        self.limpa()
        self.tabela.setRowCount(0)
        for cadc in self.cc:
            self.add_linha(cadc)

    def add_linha(self, cadc):
        rowCount = self.tabela.rowCount()
        self.tabela.insertRow(rowCount)

        id = QTableWidgetItem(str(cadc.id))
        nome = QTableWidgetItem(cadc.nome)
        telefone = QTableWidgetItem(cadc.telefone)

        self.tabela.setItem(rowCount, 0, id)
        self.tabela.setItem(rowCount, 1, nome)
        self.tabela.setItem(rowCount, 2, telefone)

    def cancelar_cliente(self):
        self.close()

    def limpa(self):
        self.nome.clear()
        self.telefone.clear()