# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-10-16 15:43:53
@UpdateDate: 2019-10-22 15:21:19
@Description: UE4样式的Slider
'''

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


def float_equal(a: float, b: float)->bool:
    if abs(a - b) < 1e-6:
        return True
    return False


class UE4Slider(QtWidgets.QWidget):
    MAX = 99999999

    def __init__(self, parent=None):
        super().__init__(parent)
        self.speed = 10
        self.spin = None
        self.value = 0
        self.range = None
        self.startpos = None
        self.bmove = False
        self.mousepos = None
        self._initSpin()
        self._init()

    def _init(self):
        self.resize(200, 30)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.spin)

    def _initSpin(self):
        self.spin = QtWidgets.QDoubleSpinBox(self)
        self.spin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spin.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.spin.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.spin.setStyleSheet("background: rgba(0,0,0,0);")
        self.spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.setRange(-self.MAX, self.MAX)

    def setRange(self, l, r):
        self.range = (l, r)
        self.spin.setRange(l, r)

    def setSpeed(self, speed):
        self.speed = speed

    def setValue(self, value):
        self.value = value
        self.spin.setValue(value)

    def setDecimals(self, prec: int):
        self.spin.setDecimals(prec)

    def wheelEvent(self, wheelEvent):
        pass

    def enterEvent(self, event):
        super().enterEvent(event)
        self.setCursor(QtCore.Qt.SizeHorCursor)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setCursor(QtCore.Qt.ArrowCursor)

    def paintEvent(self, paintEvent):
        super().paintEvent(paintEvent)
        painter = QtGui.QPainter(self)
        size = self.size()
        w, h = size.width(), size.height()
        minimum, maximum = self.range
        w = (self.value - minimum) * w / (maximum - minimum)
        pen = QtGui.QPen(QtCore.Qt.red)
        brush = QtGui.QBrush(QtCore.Qt.red)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(0, 0, w, h)
        painter.end()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.startpos = event.pos()
        self.mousepos = self.mapToGlobal(event.pos())
        self.bmove = False

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if not self.startpos:
            return
        self.setCursor(QtCore.Qt.BlankCursor)
        self.bmove = True
        pos = event.pos()
        movex = pos.x() - self.startpos.x()
        self._MoveX(movex)
        QtGui.QCursor.setPos(self.mousepos)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.startpos = None
        self.setCursor(QtCore.Qt.SizeHorCursor)
        if self.bmove:
            return
        self.bmove = False
        self._StartEditing()

    def _MoveX(self, x):
        minimum, maximum = self.range
        if float_equal(-minimum, self.MAX) and float_equal(maximum, self.MAX):
            # 没有限制的情况下
            value = self.value + (self.value - minimum + 1) * x * self.speed / (maximum - minimum)
        else:
            value = self.value + (maximum - minimum) * x * self.speed / 1000

        if value > maximum:
            value = maximum
        elif value < minimum:
            value = minimum
        self.setValue(value)

    def _StartEditing(self):
        self.spin.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
        self.spin.editingFinished.connect(self._EditingFinished)
        self.spin.setFocus()
        self.spin.selectAll()

    def _EditingFinished(self):
        value = self.spin.value()
        self.spin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spin.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.spin.editingFinished.disconnect(self._EditingFinished)
        self.setFocus()
        self.setValue(value)


class SampleWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        hbox = QtWidgets.QVBoxLayout(self)
        self.min = QtWidgets.QLineEdit("0")
        self.max = QtWidgets.QLineEdit("0")
        self.slide = UE4Slider()
        self.slide.setDecimals(4)
        hbox.addWidget(self.slide)
        hbox.addWidget(self.min)
        hbox.addWidget(self.max)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.min.editingFinished.connect(self._Min)
        self.max.editingFinished.connect(self._Min)

    def _Min(self):
        minimum = float(self.min.text())
        maximum = float(self.max.text())
        if float_equal(minimum, 0) and float_equal(maximum, 0):
            self.slide.setRange(-99999999, 99999999)
            return
        if minimum < maximum:
            self.slide.setRange(minimum, maximum)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    obj = SampleWidget()
    obj.show()
    sys.exit(app.exec_())
