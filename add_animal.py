import pymysql
import sys

import math
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QWidget, QTableWidget,
    QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox


class add_animal_w(QMainWindow):
    def __init__(self, parent=None):
            super().__init__(parent)

            # self.setFixedSize(425, 555)
            self.setWindowTitle('add_animal_w')
            uic.loadUi('add_animal_w.ui', self)

            # этот файл в одной папке с ui
            # self.lineEdit.setPlaceholderText("0")
            self.exit.clicked.connect(self.exx)
            # self.pushButton.clicked.connect(self.input_value)
            # self.one.clicked.connect(lambda: self.Num_bat(1))
            # self.two.clicked.connect(lambda: self.Num_bat(2))
            # self.three.clicked.connect(lambda: self.Num_bat(3))
            # self.sum_but.clicked.connect(self.deystvie_sum)
            # self.result.clicked.connect(self.resultat)
            # self.erase.clicked.connect(self.eraser)
            # self.cleare.clicked.connect(self.clearer)

    def exx(self):
        sys.exit()

app = QApplication(sys.argv)
w = add_animal_w()
w.show()
sys.exit(app.exec_())