from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import sys,json

from clickableWidget import ClickableQLabel


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('search.ui', self)

        self.lineedit = self.findChild(QLineEdit,'searchLineEdit')

        self.label = self.findChild(ClickableQLabel,'searchLabel')
        self.label.clicked.connect(self.search)

        self.setWindowTitle('SEARCH')

        self.show()
    
    @pyqtSlot
    def search(self):
        self.hide()
        self.r = Result()
        self.r.showContent(self,self.lineedit.text())


class Result(QWidget):
    def __init__(self):
        super(Result,self).__init__()
        uic.loadUi('result.ui',self)
        self.setWindowTitle('RESULT')
    
    def showContent(self,parent,keyWord):
        self.parent = parent
        self.show()
    
    def getContent(self,keyWord):
        keyWord = keyWord+'.json'
        f = open(keyWord,encoding='utf-8')
        content = f.read()
        content = json.loads(content)
        content = content['data']

    def constructTable(content):
        pass

    def closeEvent(self,event):
        if self.parent.isHidden():
            self.parent.setHidden(False)


'''
def handleJson(name):
    name = name+'.json'
    f = open(name,encoding='utf-8')
    content = f.read()
    content = json.loads(content)
    #print(content)
'''


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
