from qt_core import *
import model.doces_dao as doces_dao
import model.clientes_dao as clientes_dao


class CadVenda(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('cadastrovendas.ui', self)
        
        # listas
        self.lista_doces = None
        self.lista_clientes = None
        self.lista_itens = None

        # cliente e doce atual
        self.cliente_atual = None
        self.doce_atual = None

        # botões
        self.add_item.clicked.connect(self.add_item_list)
        self.finalizecad.clicked.connect(self.finalizar_cad)
        self.cancelecad.clicked.connect(self.cancelar_cad)

        self.carrega_cliente()
        self.carrega_doce()

    def add_item_list(self):
        if self.quantidade.text() == '' or self.valor_venda_cad.text() == '':
            print('Dados obrigatórios *')
        else:
            # cria novo item
            """item = {'quantidade': self.quantidade.text(),
                'doce': self.doce_atual}
            # adiciona na lista de itens
            self.lista_itens.append(item)"""

            self.atualiza_dados_cad_venda()

    def atualiza_dados_cad_venda(self):
        pass
        # atualiza a quantidade de itens
        # mostra o tamanho da lista itens
        # atualiza total pago/a pagar
        # somar valores da multiplicaçao entre a quantidade itens * valor do doce

    def carrega_cliente(self):
        # lista clientes
        self.lista_clientes = clientes_dao.lista_clientes
        # armazena nomes dos clientes
        lista = []
        for c in self.lista_clientes:
            lista.append(c.nome)
        # lista nomes dos clientes
            """CONCLUIR"""
        # pega o INDEX do cliente selecionado

    def carrega_doce(self):
        # lista doces
        self.lista_doces = doces_dao.lista_doces
        for d in self.lista_doces:
           # self.doces_listWidget.addItem(d.nome)

        #self.pecas_listWidget.currentRowChanged.connect(self.pega_peca) # PARA LEMBRAR

            """CONCLUIRRRR"""
    #def pega_doce(self):

    #def pega_cliente(self):

    def finalizar_cad(self):
        print(f"Cliente: {self.cliente_atual.nome}")

    def cancelar_cad(self):
        # fecha janela
        self.close()