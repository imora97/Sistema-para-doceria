from qt_core import*

class ChamaZap(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/zap.ui', self)
        