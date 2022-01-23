from qt_core import*

class beijinho(QWidget):

    def __init__(self, janela_cadastro):
        super().__init__()
        uic.loadUi('view/beijinho.ui', self)
        
        self.janela_cadastro = janela_cadastro
