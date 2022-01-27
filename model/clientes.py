
class Clientes():

    def __init__(self, id, nome, endereço):
        self.id = id
        self.nome = nome
        self.endereço = endereço

    def imprime(self):
        print(f'{self.id}, {self.nome}, {self.endereço}')