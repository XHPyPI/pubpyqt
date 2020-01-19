# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-12-17 10:56:13
@UpdateDate: 2019-12-17 13:28:55
@Description: 分隔控件
'''

import sys

from PyQt5 import QtCore, QtWidgets

TEST_INFO = {
    "group1" : ["lable1", "lable2"],
    "group2" : ["lable1", "lable2", "lable3"],
    "group3" : ["lable1", "lable2"],
}


class SplitWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        vBox = QtWidgets.QVBoxLayout(self)
        for group, labels in TEST_INFO.items():
            proxy_widget = ProxyWidget(group)
            vBox.addWidget(proxy_widget)
            for label in labels:
                child_widget = ChildWidget(label, self)
                proxy_widget.add_widget(child_widget)


class ProxyWidget(QtWidgets.QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self._widget_list = []
        self._name = name
        self._init_ui()

    def _init_ui(self):
        vBox = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel(self._name)
        self._container = QtWidgets.QWidget()
        vContainerBox = QtWidgets.QVBoxLayout(self._container)
        vContainerBox.setSpacing(0)
        vContainerBox.setContentsMargins(0, 0, 0, 0)
        vBox.addWidget(label)
        vBox.addWidget(self._container)

    def add_widget(self, widget):
        self._container.layout().addWidget(widget)
        self._widget_list.append(widget)


class ChildWidget(QtWidgets.QWidget):
    def __init__(self, label, parent=None):
        super().__init__(parent)
        self._label = label
        self._init_ui()

    def _init_ui(self):
        hBox = QtWidgets.QHBoxLayout(self)
        label = QtWidgets.QLabel(self._label, self)
        label.move(0, 0)
        self._vertical_line = LineWidget(self)
        self._vertical_line.move(150, 0)
        line = QtWidgets.QLineEdit(self._label, self)
        line.move(160, 0)
        hBox.addWidget(label)
        # hBox.addWidget(line)


class LineWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.VLine | QtWidgets.QFrame.Plain)
        self.resize(3, 25)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    obj = SplitWidget()
    obj.show()
    sys.exit(app.exec_())
