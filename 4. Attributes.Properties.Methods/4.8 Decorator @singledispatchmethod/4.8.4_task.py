from functools import singledispatchmethod
from datetime import date
from dateutil.relativedelta import relativedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')
    
    @__init__.register
    def _from_ISO(self, birth_date: str):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')   
    
    @__init__.register
    def _from_sequence(self, birth_date: list | tuple):
        try:
            self.birth_date = date(*birth_date)
        except :
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        return relativedelta(date.today(), self.birth_date).years
        return relativedelta(date.today(), self.birth_date).years
