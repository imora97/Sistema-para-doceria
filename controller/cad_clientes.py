from qt_core import *
import model.clientes_dao as clientes_dao


class CadCliente(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/cadastroclientes.ui', self)

        # insere tabela no layout
        #self.table = TabelaCliente(self)
        
        self.cliente_atual = None

        # lista
        self.lista_clientes = None

        self.salvar.clicked.connect(self.salvar_cliente)
        self.cancelar.clicked.connect(self.cancelar_cliente)
        self.limpa.clicked.connect(self.limpar)
        self.excluir_button.clicked.connect(self.excluir)
    
    def salvar_cliente(self):
        if self.nome.text() == '' or self.telefone.text() == '':
            print('\033[7;35;44mDados obrigatórios *\033[m') #código de cor da fonte

        else:
            print('\033[4;35mLogin salvo com sucesso\033[m')
            
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

    def excluir(self):
        if self.cliente_atual != None:
            clientes_dao.delete(self.cliente_atual.id)
            self.carrega_dados()
            
            ##### COLOCAR COMANDO DE CAIXA DE SELEÇÃO

    def limpar(self):
        self.nome.clear()
        self.telefone.clear()