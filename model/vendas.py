
class Vendas():

    def __init__(self, id, item, quantidade, tipo, valor):
        self.id = id
        self.item = item
        self.quantidade = quantidade
        self.tipo = tipo
        self.valor = valor

    def imprime(self):
        print(f'{self.id}, {self.item}, {self.quantidade}, {self.tipo}, {self.valor}')