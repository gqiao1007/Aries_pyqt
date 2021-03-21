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

        msg.label_pix.setPixmap(QPixmap("./res/"+"1.png"))

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
        msg2.label.setText(weather0["text_day"])
        msg2.label_9.setPixmap(QPixmap("./res/" + weather0["code_day"] + ".png"))
        msg2.label_4.setText(weather0["text_night"])
        msg2.label_10.setPixmap(QPixmap("./res/" + weather0["code_night"] + ".png"))
        msg2.label_11.setText(weather0["high"])
        msg2.label_12.setText(weather0["low"])
        msg2.label_13.setText(weather0["wind_direction"])
        msg2.label_14.setText(weather0["wind_scale"])


        msg3 = Ui_Form()
        c = QWidget()
        msg3.setupUi(c)
        msg3.label.setText(weather1["text_day"])
        msg3.label_9.setPixmap(QPixmap("./res/" + weather1["code_day"] + ".png"))
        msg3.label_4.setText(weather1["text_night"])
        msg3.label_10.setPixmap(QPixmap("./res/" + weather1["code_night"] + ".png"))
        msg3.label_11.setText(weather1["high"])
        msg3.label_12.setText(weather1["low"])
        msg3.label_13.setText(weather1["wind_direction"])
        msg3.label_14.setText(weather1["wind_scale"])

        msg4 = Ui_Form()
        d = QWidget()
        msg4.setupUi(d)
        msg4.label.setText(weather2["text_day"])
        msg4.label_9.setPixmap(QPixmap("./res/" + weather2["code_day"] + ".png"))
        msg4.label_4.setText(weather2["text_night"])
        msg4.label_10.setPixmap(QPixmap("./res/" + weather2["code_night"] + ".png"))
        msg4.label_11.setText(weather2["high"])
        msg4.label_12.setText(weather2["low"])
        msg4.label_13.setText(weather2["wind_direction"])
        msg4.label_14.setText(weather2["wind_scale"])


        return b,c,d,weather0["date"], weather1["date"], weather2["date"]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    we = Weather()
    we.show()
    sys.exit(app.exec_())




