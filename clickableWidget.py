#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
from PyQt5 import QtCore,QtWidgets


class ClickableQLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()
    def __init(self, parent):
        QtWidgets.QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()