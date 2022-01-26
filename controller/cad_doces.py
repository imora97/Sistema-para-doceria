from model.doces import Doces
import model.doces_dao as doces_dao
from qt_core import *


class CadDoce(QWidget):

    def __init__(self, janela_doces):
        super().__init__()
        uic.loadUi("view/cadastrodoces.ui", self)

        self.janela_doces = janela_doces

        self.finalizar.clicked.connect(self.salvar_doce)
        self.cancelar.clicked.connect(self.cancelar_doce)

    def salvar_doce(self):
        # pegar os dados lançados 
        nome = self.nome.text()
        peso = self.peso.text()
        tipo = self.tipo.items() #***
        valor = self.valor.text()

        if self.nome.text() == '' or self.peso.text() == '' or self.valor.text() == '':
            print('Dados obrigatórios *')
        else:
            # cria novo item
            item_1 = {'nome': self.nome.text(),
            'peso': self.peso.text(),
            'tipo': self.tipo.text(),
            'valor': self.valor.text()} # O QUE É ISSO????


        # cria o cadastro 
        """novo_doce = Doces(None, nome, peso, tipo, valor)
        doces_dao.adicionar(novo_doce)""" # ESSE 'NOVO DOCE' SAIU DE ONDE, PELO AMOR DE PAI??!

        # atualiza tabela
        self.janela_doces.carrega_dados() ####* NÃO TEM FUNÇÃO??
        
        # fecha janela
        self.close()

    def cancelar_doce(self):
        # fecha janela
        self.close()
