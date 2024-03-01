import sys
import json
import connect_db
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QWidget, QTableWidget,
    QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView)



class Window_home_animal(QMainWindow):  # Всплывающее окно добавления домашнего животного
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Добавление животного')
        uic.loadUi('add_home_animal_window.ui', self)
        # self.setFixedSize(405, 175)
        self.save_btn.clicked.connect(self.save)
        self.esc_btn.clicked.connect(self.exx)

    def save(self):  # Зипась в фаил
        self.textEdit.setPlaceholderText("Контакт сохранен")

    def exx(self):  # Закрыть всплывающее окно
        self.close()



class Window_v_animal(QMainWindow):  # Всплывающее окно добавления вьючного животного
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Добавление животного')
        uic.loadUi('add_v_animal_window.ui', self)
        self.save_btn.clicked.connect(self.save)
        self.esc_btn.clicked.connect(self.exx)

    def save(self):  # Зипась в фаил
        with open("phone-book.json", "r", encoding="utf-8") as book1:
            pb = json.load(book1)
        name = (self.lineEdit_2.text())
        name2 = (self.lineEdit_3.text())
        number0 = (self.lineEdit_5.text())
        pb[name] = {"name2": name2, "phone_numbers": number0}
        with open("phone-book.json", "r+", encoding="utf-8") as book:
            book.write(json.dumps(pb, ensure_ascii=False))
        self.textEdit.setPlaceholderText("Контакт сохранен")



    def exx(self):  # Закрыть всплывающее окно
        self.close()


class Window_all_animal(QMainWindow):  # Всплывающее окно все животные
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Все животные')
        uic.loadUi('all_animal_window.ui', self)
        # self.setFixedSize(405, 175)
        # self.pushButton.clicked.connect(self.show_b)
        self.esc_btn.clicked.connect(self.exx)

        self.pushButton.clicked.connect(self.show_b)

        #####################
    # @pyqtSlot(bool)
    def show_b(self):

        result = connect_db.connect()
        if result:
            self.tableWidget.setRowCount(len(result))

            for row, item in enumerate(result):
                column_l_item = QTableWidgetItem(str(item['id']))
                column_2_item = QTableWidgetItem(str(item['firstname']))

                self.tableWidget.setItem(row, 0, column_l_item)
                self.tableWidget.setItem(row, 1, column_2_item)

            # eLse:
            #     QMessageBox.Information(self, 'Нет подключения')
            #     return

    # def show_b(self):  # показать
    #     connect_db.connect()

        # pass

    def exx(self):  # Закрыть всплывающее окно
        self.close()


class MainWindow(QMainWindow):  # Основное окно
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.setFixedSize(370, 435)
        self.setWindowTitle('Животные')
        uic.loadUi('main_window.ui', self)
        self.add_h_animal.clicked.connect(self.window_new_home_animal)
        self.add_v_animal.clicked.connect(self.window_new_v_animal)
        self.show_animal.clicked.connect(self.window_show_animal)
        self.take_command.clicked.connect(self.window_take_command)
        self.exit.clicked.connect(self.exx)

    def window_new_home_animal(self):
        self.window = Window_home_animal(self)
        self.window.show()

    def window_new_v_animal(self):
        self.window = Window_v_animal(self)
        self.window.show()

    def window_show_animal(self):
        connect_db.connect()
        self.window = Window_all_animal(self)
        self.window.show()



    def window_take_command(self):
        pass


    def exx(self):  # Закрыть всплывающее окно
        sys.exit()





app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

