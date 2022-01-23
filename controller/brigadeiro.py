from qt_core import*

class brigadeiro(QWidget):

    def __init__(self, janela_cadastro):
        super().__init__()
        uic.loadUi('view/brigadeiro.ui', self)
        
        self.janela_cadastro = janela_cadastro
