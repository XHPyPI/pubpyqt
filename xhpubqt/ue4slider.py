# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-10-16 15:43:53
@UpdateDate: 2019-10-21 17:47:20
@Description: UE4樣式的Slider
创建一个材质，然后创建一个 ScalarParameter,输入SliderMin和SliderMax，对于Value的范围限制不会马上生效
'''

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class UE4Slider(QtWidgets.QDoubleSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(200, 30)
        self._init()
        print(self.maximum(), self.minimum())

    def _init(self):
        self.lineEdit().setReadOnly(True)
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
        w = (self.value() - self.minimum()) * w / (self.maximum() - self.minimum())
        pen = QtGui.QPen(QtCore.Qt.red)
        brush = QtGui.QBrush(QtCore.Qt.red)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(0, 0, w, h)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.startpos = event.pos()
        print("start pos:", self.startpos)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if not self.startpos:
            return
        pos = event.pos()
        movex = pos.x() - self.startpos.x()
        self.startpos = pos
        self._MoveX(movex)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.startpos = None

    def _MoveX(self, x):
        value = self.value() + (self.value() - self.minimum() + 1) * x / (self.maximum() - self.minimum()) / 10
        print("move value:", self.value(), x, value)
        if value > self.maximum():
            value = self.maximum()
        elif value < self.minimum():
            value = self.minimum()
        self.setValue(value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    obj = UE4Slider()
    obj.show()
    sys.exit(app.exec_())
