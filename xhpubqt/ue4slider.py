# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-10-16 15:43:53
@UpdateDate: 2019-10-18 17:14:49
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
        self.slider = None
        # self.setStyleSheet("background: rgba(0,0,0,0);")
        self.resize(200, 30)
        # self.lineEdit = UE4LineEdit(self)
        # self.setLineEdit(self.lineEdit)
        # self.setReadOnly(True)
        self._initslider()

    def _init(self):
        self.setFocusPolicy(QtCore.Qt.NoFocus)

    def _initslider(self):
        self.slider = QtWidgets.QDoubleSpinBox(self)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.slider)
        vbox.setContentsMargins(0, 0, 0, 0)

        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.slider.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background: rgba(0,0,0,0);")
        self.slider.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.slider.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)

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
