# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-10-16 15:43:53
@UpdateDate: 2019-10-16 16:27:02
@Description: UE4樣式的Slider
'''

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class UE4LineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def enterEvent(self, event):
        self.setCursor(QtCore.Qt.SizeHorCursor)

    def leaveEvent(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)


class UE4Slider(QtWidgets.QDoubleSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setStyleSheet("background: rgba(0,0,0,0);")
        self.resize(200, 30)
        # self.lineEdit = UE4LineEdit(self)
        # self.setLineEdit(self.lineEdit)
        self.setReadOnly(True)

    def _initslider(self):
        pass

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
