# _*_ coding: utf-8 _*_

import requests

class GetWeatherInfo():

    def __init__(self, flag, city):
        '''
        一些初始设置
        '''
        self.flag = flag
        # flag表示的是查询天气的类型：实时天气还是近三天天气
        if city == "北京":
            self.city = "beijing"
        elif city == "上海":
            self.city = "shanghai"
        else:
            self.city = "guangzhou"
        # city表示的是我们查询的城市
        self.real_time = "https://api.seniverse.com/v3/weather/now.json?key=SE2ZrQ-qK-OjeTGo5&location=beijing&language=zh-Hans&unit=c"
        self.nearly_3_days = "https://api.seniverse.com/v3/weather/daily.json?key=SE2ZrQ-qK-OjeTGo5&location=beijing&language=zh-Hans&unit=c&start=0&days=5"

    def getweather(self):
        if self.flag == 0:
            # 实时天气
            widc = self.internet(self.real_time)
            if widc:
                weather = widc["results"][0]["now"]["text"]
                weather_code = widc["results"][0]["now"]["code"]
                weather_temperature = widc["results"][0]["now"]["temperature"]
                last_update = widc["results"][0]["last_update"]
                return weather, weather_code, weather_temperature, last_update

        elif self.flag == 1:
            widc = self.internet(self.nearly_3_days)
            if widc:
                weather0 = widc["results"][0]["daily"][0]
                weather1 = widc["results"][0]["daily"][1]
                weather2 = widc["results"][0]["daily"][2]
                return weather0, weather1, weather2

    def internet(self, url):
        '''
        requests库访问API，获取天气信息
        '''
        r = requests.get(url)
        weatherinfo = r.text
        weatherinfo_dic = eval(weatherinfo)
        # 将其直接转换成字典类型
        if "status_code" in weatherinfo_dic:
            return 0
        return weatherinfo_dic
