from abc import ABC, abstractmethod
from datetime import date as dt

class CountryDate(ABC):
    def __init__(self, year, month, day):
        self.date = dt(year, month, day)

    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return self.date


class USADate(CountryDate):
    def format(self):
        return self.date.strftime('%m-%d-%Y')
        
class ItalianDate(CountryDate):
    def format(self):
        return self.date.strftime('%d/%m/%Y')