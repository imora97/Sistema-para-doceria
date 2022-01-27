from controller.cad_vendas import CadVenda

class add_item():

    def __init__(self, id, quantidade, tipo, valor):
        self.id = id
        self.quantidade = quantidade
        self.tipo = tipo
        self.valor = valor

    def imprime(self, lista_itens, doce_atual):

        self.lista_itens = None ##### nem sei se precisa e nem sei se é assim
        self.doce_atual = None

        print(f'{self.id}, {self.quantidade}, {self.tipo}, {self.valor}{self.lista_itens}, {self.doce_atual}')