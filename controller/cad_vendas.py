from qt_core import *
import model.doces_dao as doces_dao
import model.clientes_dao as clientes_dao


class CadVenda(QWidget):

    def __init__(self, janela_vendas):
        super().__init__()
        uic.loadUi('view/cadastrovendas.ui', self)
        
        # listas
        self.lista_doces = None
        self.lista_clientes = None
        self.lista_itens = None

        # cliente e doce atual
        self.cliente_atual = None
        self.doce_atual = None

        self.janela_vendas = janela_vendas

        # botões
        self.add_item.clicked.connect(self.add_item_list)
        self.finalizecad.clicked.connect(self.finalizar_cad)
        self.cancelecad.clicked.connect(self.cancelar_cad)
        self.limpar.clicked.connect(self.limpa)

        self.carrega_cliente()
        self.carrega_doce()

    def add_item_list(self):
        if self.quantidade.text() == '' or self.valor_venda_cad.text() == '' or self.tipo.currentText() == '' or self.item.currentText() == '':
            print('Dados obrigatórios *')
        else:
            # cria novo item
            item = {'quantidade': self.quantidade.text(),
                'doce': self.doce_atual}
            self.lista_itens.append(item)

            self.atualiza_dados_cad_venda()

    def atualiza_dados_cad_venda(self):
        pass
        # atualiza a quantidade de itens
        # mostra o tamanho da lista itens
        # atualiza total pago/a pagar
        # somar valores da multiplicaçao entre a quantidade itens * valor do doce

    def carrega_cliente(self):
        self.lista_clientes = clientes_dao.lista_clientes
        lista = []
        for c in self.lista_clientes:
            lista.append(c.nome)
            #________________________________CONCLUIR
        # pega o INDEX do cliente selecionado

    def carrega_doce(self):
        self.lista_doces = doces_dao.lista_doces
        for d in self.lista_doces:
           self.doces_listWidget.addItem(d.nome)

        #self.pecas_listWidget.currentRowChanged.connect(self.pega_peca) ##### PARA LEMBRAR

            #________________________________CONCLUIR
    #def pega_doce(self):

    #def pega_cliente(self):

    def finalizar_cad(self):
        if self.item.currentText() == '' or self.quantidade.text() == '' or self.tipo.currentText() == '' or self.valor.text() == '':
            print('Dados obrigatórios *')
        else:
            print(f"Cliente: {self.cliente_atual.nome}")
            print
            
            self.close()

    def cancelar_cad(self):
        self.close()

    def limpa(self):
        self.item.clear()
        self.quantidade.clear()
        self.tipo.clear()
        self.valor_venda_cad.clear()
