
class Clientes():

    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def imprime(self):
            print(f'{self.id}, {self.nome}, {self.telefone}')