# _*_ coding: utf-8 _*_


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication,QMainWindow

from PyQt5.QtGui import QPixmap


from main_ui import Ui_MainWindow
from GetWeather import GetWeatherInfo
from realweather import Ui_RealTime
from threedaysweather import Ui_Form
import sys


class Weather(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Weather, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
        self.flag = 0

    def initUi(self):
        self.showrealweather()

    @pyqtSlot(bool)
    def on_radioButton_toggled(self, checked):
        """
        实时天气
        """
        self.flag = 0

    @pyqtSlot(bool)
    def on_radioButton_2_toggled(self, checked):
        """
        近3天天气
        """
        self.flag = 1

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        查询天气：根据查询天气的种类，在选项卡上展示页面。实时天气就展示一个，近三天天气就展示3个
        """
        if self.flag == 0:
            self.showrealweather()
        else:
            t0, t1, t2, d0, d1, d2 = self.showthreedaysweather()
            self.tabWidget.addTab(t0, d0)
            self.tabWidget.addTab(t1, d1)
            self.tabWidget.addTab(t2, d2)

    def showrealweather(self):
        city = self.comboBox.currentText()
        ww = GetWeatherInfo(0, city)
        weather, weather_code, weather_temperature, last_update = ww.getweather()
        print(weather_temperature)
        print(weather)


        msg = Ui_RealTime()
        a = QWidget()
        msg.setupUi(a)
        msg.weathernumber.setText(weather_temperature)
        msg.weatherwhat.setText(weather)

        update = "天气最新更新时间--" + last_update[11:16]
        # # 只取更新时间的具体时间（几点几分），否则还有某年某月等内容
        #
        self.tabWidget.clear()
        # # 之前有选项卡的清空
        #
        self.tabWidget.addTab(a, update)

    def showthreedaysweather(self):
        city = self.comboBox.currentText()
        ww = GetWeatherInfo(1, city)
        self.tabWidget.clear()
        weather0, weather1, weather2 = ww.getweather()
        msg2 = Ui_Form()
        b = QWidget()
        msg2.setupUi(b)

        msg3 = Ui_Form()
        c = QWidget()
        msg3.setupUi(c)

        msg4 = Ui_Form()
        d = QWidget()
        msg4.setupUi(d)

        return b,c,d,weather0["date"], weather1["date"], weather2["date"]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    we = Weather()
    we.show()
    sys.exit(app.exec_())




