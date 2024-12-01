from datetime import datetime as dt

class LoggerMixin:
    def log(self, level, text):
        current_date = dt.now().strftime('%d.%m.%Y %H:%M:%S')
        print(f'[{current_date}] - {level} - {self.__class__.__name__}: {text}')
