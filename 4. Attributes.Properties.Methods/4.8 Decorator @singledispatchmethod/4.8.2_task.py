from functools import singledispatchmethod

class Negator:
    def __init__(self):
        pass

    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register
    @staticmethod
    def _from_bool(obj: bool):
        return not obj

    @neg.register
    @staticmethod
    def _from_num(obj: int | float):
        return -obj
    
    
