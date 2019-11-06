# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-11-06 16:27:05
@UpdateDate: 2019-11-06 19:38:39
@Description: 进度条提示
'''

import sys

from PyQt5 import QtCore, QtWidgets


class ProgressTip(QtWidgets.QProgressDialog):
    """进度条提示
    用于在处理长时间任务时，界面会卡主对于用户不友好，可以使用进度条提示做反馈
    """

    def __init__(self, tip="waiting...", parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(1000, 50)
        self.setRange(0, 100)
        self.setLabelText(tip)
        self.setCancelButton(None)
        self.setAutoClose(True)
        self.open()


class TestWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        hbox = QtWidgets.QHBoxLayout(self)
        btn = QtWidgets.QPushButton("开始", self)
        hbox.addWidget(btn)
        btn.clicked.connect(self.Start)

    def Start(self):
        import time
        progress = ProgressTip("Test")
        progress.open()
        for x in range(101):
            time.sleep(0.1)
            progress.setValue(x)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    obj = TestWidget()
    obj.show()
    sys.exit(app.exec_())
