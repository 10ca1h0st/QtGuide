from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot,pyqtSignal
import sys,json

from result import Result
from clickableWidget import ClickableQLabel


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./UI/search.ui', self)

        self.lineedit = self.findChild(QLineEdit,'searchLineEdit')

        self.label = self.findChild(ClickableQLabel,'searchLabel')
        self.label.clicked.connect(self.search)

        self.setWindowTitle('SEARCH')

        self.show()
    
    @pyqtSlot()
    def search(self):
        self.hide()
        self.r = Result()
        self.r.showContent(self,self.lineedit.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
