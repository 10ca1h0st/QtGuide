from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys,os

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
        print(self.lineedit.text())

if __name__ == '__main__':
    print(os.getcwd())
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()