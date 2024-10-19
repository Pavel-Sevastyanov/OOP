from functools import singledispatchmethod

class Processor:
    def __init__(self):
        pass
    
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register
    @staticmethod
    def _from_int(data: int | float):
        return data * 2

    @process.register
    @staticmethod
    def _from_str(data: str):
        return data.upper()

    @process.register
    @staticmethod
    def _from_list(data: list):
        return sorted(data)

    @process.register
    @staticmethod
    def _from_int(data: tuple):
        return tuple(sorted(data))
