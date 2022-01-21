from controller.main_window import MainWindow
from qt_core import *
from controller.main_window import MainWindow

app = QApplication(sys.argv)

win = MainWindow()
win.show()

sys.exit(app.exec())