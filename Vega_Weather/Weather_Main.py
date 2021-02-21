# _*_ coding: utf-8 _*_


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow
from PyQt5.QtGui import QPixmap


from main_ui import Ui_MainWindow
import sys


class Weather(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Weather, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.flag = 0

    def initUi(self):
        self.show_weather()


    def show_weather(self):
        city = self.comboBox.currentText()
        print(city)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    we = Weather()
    we.show()
    sys.exit(app.exec_())




