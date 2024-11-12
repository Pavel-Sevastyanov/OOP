import datetime

class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date):
        print(date.strftime('%d.%m.%Y'))
        super().rain()  

    def snow(self, date):
        print(date.strftime('%d.%m.%Y'))
        super().snow()

    def low_temperature(self, date):
        print(date.strftime('%d.%m.%Y'))
        super().low_temperature()            