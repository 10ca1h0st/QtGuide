from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import json

class Result(QWidget):
    def __init__(self):
        super(Result,self).__init__()
        uic.loadUi('./UI/result.ui',self)
        self.setWindowTitle('RESULT')

        self.table = self.findChild(QTableWidget,'content')

        self.pre = self.findChild(QPushButton,'pre')
        self.next = self.findChild(QPushButton,'next')

        self.pre.clicked.connect(self.prePage)
        self.next.clicked.connect(self.nextPage)
    
    @pyqtSlot()
    def prePage(self):
        print('press pre button')
        if self.item_index<10:
            return
        else:
            print('go to pre page')
            self.item_index = self.item_index-10
            self.fillTable(self.item_index)

    @pyqtSlot()
    def nextPage(self):
        print('press next page')
        if self.item_index+10>=self.item_num:
            return
        else:
            print('go to next page')
            self.item_index = self.item_index+10
            self.fillTable(self.item_index)
    
    def showContent(self,parent,keyWord):
        self.parent = parent
        if self.getContent(keyWord):
            self.show()
        else:
            self.parent.setHidden(False)
    

    #return None means error
    def getContent(self,keyWord):
        keyWord = keyWord+'.json'
        try:
            f = open(keyWord,encoding='utf-8')
        except FileNotFoundError:
            QMessageBox.critical(self,"错误","没有发现有效信息")
            return
        content = f.read()
        content = json.loads(content)
        self.content = content['data']
        self.constructTable()
        return 1

    '''
    目前的想法是一页10行
    '''
    def constructTable(self):
        column_num = len(self.content[0].keys())
        row_num = 10

        self.table.setRowCount(row_num)
        self.table.setColumnCount(column_num)

        #set the name of each column
        self.table.setHorizontalHeaderLabels(self.content[0].keys())
        #set table not editable
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #set vertical header invisible
        #self.table.verticalHeader().setVisible(False)

        #自适应宽度
        #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #自适应高度
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #目前从第几条数据开始显示
        self.item_index = 0

        #共有几条数据
        self.item_num = len(self.content)

        self.fillTable(self.item_index)

    #从数据的第index项开始填充表格
    def fillTable(self,index):
        self.table.clearContents()
        for i in range(10):
            if index+i>=self.item_num:
                break
            each_row = self.content[index+i]
            for column,cell in enumerate(each_row.values()):
                self.table.setItem(i,column,QTableWidgetItem(cell))


            



    def closeEvent(self,event):
        if self.parent.isHidden():
            self.parent.setHidden(False)
