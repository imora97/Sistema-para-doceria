from model.doces import Doces
import model.doces_dao as doces_dao
from qt_core import *



class Cadastro(QWidget):
    def __init__(self, janela_doces):
        super().__init__()
        uic.loadUi("view/cadastro.ui", self)

        self.janela_doces = janela_doces

        self.salvar.clicked.connect(self.salvar_doce)
        self.cancelar.clicked.connect(self.cancelar_doce)

    def salvar_doce(self):
        # pegar os dados lançados 
        nome = self.nome.text()
        peso = self.peso.text()
        tipo = self.tipo.value()
        valor = self.valor.text() #***

        # cria o cadastro 
        novo_doce = Doces(None, nome, peso, tipo, valor)
        doces_dao.adicionar(novo_doce)

        # atualiza tabela # CONCLUIR
        self.janela_doces.carrega_dados()
        
        # fecha janela
        self.close()

    def cancelar_doce(self):
        # fecha janela
        self.close()
