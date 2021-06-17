# -*- coding: utf-8 -*-

"""
这是一个极简图书管理（QTableWidget的使用）的例子！
文章链接：http://www.xdbcb8.com/archives/779.html
文章链接：http://www.xdbcb8.com/archives/784.html
文章链接：http://www.xdbcb8.com/archives/795.html
文章链接：http://www.xdbcb8.com/archives/814.html
"""

import sys
from Mbook import MainBook

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mb = MainBook()
    mb.show()
    sys.exit(app.exec_())