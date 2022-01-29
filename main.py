from controller.main_window import MainWindow
from model.database import createDB
from qt_core import *

app = QApplication(sys.argv)

createDB()

win = MainWindow()
win.show()

sys.exit(app.exec())