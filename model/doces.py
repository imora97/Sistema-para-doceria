
# responsável pelos dados Doces
class Doces():
    
    def __init__(self, id, nome, peso, tipo, valor):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.tipo = tipo
        self.valor = valor

    def imprime(self):
        print(f'{self.id}, {self.nome}, {self.peso}, {self.tipo}, {self.valor}')