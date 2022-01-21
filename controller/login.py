from qt_core import*

class Login(QWidget):

    def __init__(self):
        super().__init()
        uic.loadUi('view/login.ui', self)
        