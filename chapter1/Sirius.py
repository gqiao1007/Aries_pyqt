import pydesigner_test   # 需要运行的.py文件名

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建应用程序
    mainwindow = QMainWindow()      # 创建主窗口

    ui = pydesigner_test.Ui_MainWindow()      # 调用first中的主窗口

    ui.setupUi(mainwindow)          # 向主窗口添加控件

    mainwindow.show()               # 显示窗口
    sys.exit(app.exec_())           # 程序执行循环