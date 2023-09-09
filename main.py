import sys
from work_with_database import *
from forms.test_main_window import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog


#работа с формой
class MainWindow(QMainWindow, UiTestWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UiTestWindow()
        self.ui.setupUi(self)


app = QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())