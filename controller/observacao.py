from qt_core import*

class Obs(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/obs.ui', self)
        
