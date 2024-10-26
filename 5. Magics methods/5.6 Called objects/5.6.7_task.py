import datetime

class DateFormatter:
    def __init__(self, country_code):
        self.country_codes = {
                    "ru": "%d.%m.%Y",
                    "us": "%m-%d-%Y",
                    "ca": "%Y-%m-%d",
                    "br": "%d/%m/%Y",
                    "fr": "%d.%m.%Y",
                    "pt": "%d-%m-%Y"
        }
        self.code_format = self.country_codes[country_code]

    def __call__(self, d):
        return d.strftime(self.code_format)