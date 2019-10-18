# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-10-16 15:43:53
@UpdateDate: 2019-10-18 17:18:23
@Description: UE4樣式的Slider
'''

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class UE4Slider(QtWidgets.QDoubleSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(200, 30)
        self._init()

    def _init(self):
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background: rgba(0,0,0,0);")
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)

    def wheelEvent(self, wheelEvent):
        pass

    def enterEvent(self, event):
        self.setCursor(QtCore.Qt.SizeHorCursor)
        self.lineEdit().setCursor(QtCore.Qt.SizeHorCursor)

    def leaveEvent(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.lineEdit().setCursor(QtCore.Qt.ArrowCursor)

    def setValue(self, value):
        super().setValue(value)

    def paintEvent(self, paintEvent):
        super().paintEvent(paintEvent)
        painter = QtGui.QPainter(self)
        size = self.size()
        w, h = size.width(), size.height()
        pen = QtGui.QPen(QtCore.Qt.red)
        brush = QtGui.QBrush(QtCore.Qt.red)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(0, 0, w, h)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    obj = UE4Slider()
    obj.show()
    sys.exit(app.exec_())
