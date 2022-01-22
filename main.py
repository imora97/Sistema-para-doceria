from controller.main_window import MainWindow
from qt_core import *

app = QApplication(sys.argv)

win = MainWindow()
win.show()

sys.exit(app.exec())