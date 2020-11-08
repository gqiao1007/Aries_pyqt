# _*_ coding: utf-8 _*_
#coding = 'utf-8'

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('Arcturus ')

        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1) #增加伸缩量
        hbox.addWidget(bt1)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(bt2)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(bt3)
        hbox.addStretch(6)#增加伸缩量

        self.setLayout(hbox)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())