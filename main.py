from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

from clickableWidget import ClickableQLabel


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('search.ui', self)

        self.button = self.findChild(QPushButton, 'searchButton')
        self.button.clicked.connect(self.search)

        self.lineedit = self.findChild(QLineEdit,'searchLineEdit')

        self.label = self.findChild(ClickableQLabel,'searchLabel')
        self.label.clicked.connect(self.search)

        self.show()
    
    def search(self):
        self.r = Result()
        self.r.show()

class Result(QtWidgets.QDialog):
    def __init__(self):
        super(Result,self).__init__()
        uic.loadUi('result.ui',self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()