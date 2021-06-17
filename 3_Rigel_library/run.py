# -*- coding: utf-8 -*-


import sys
from Mbook import MainBook

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mb = MainBook()
    mb.show()
    sys.exit(app.exec_())