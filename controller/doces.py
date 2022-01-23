from qt_core import*


class DocesPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/doces.ui', self)

