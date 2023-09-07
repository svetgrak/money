import sys
from work_with_database import *
from forms.test_main_window import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog

# имя базы данных по умолчанию
name_database = "budget_project"

#create_database('budget_project')

# удалить базу данных
def delete():
    connection_psql = open_connection_psql()
    delete_database(name_database, connection_psql)
    close_connection(connection_psql)


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