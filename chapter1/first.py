# _*_ coding: utf-8 _*_
#!/usr/bin/python3
# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('start Demo gqiao')
    w.show()

    sys.exit(app.exec_())