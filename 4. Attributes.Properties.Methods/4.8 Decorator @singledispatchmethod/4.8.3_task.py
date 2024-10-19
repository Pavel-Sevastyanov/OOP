from functools import singledispatchmethod

class Formatter:
    def __init__(self):
        pass

    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    @staticmethod
    def _from_int(arg: int):
        print(f'Целое число: {arg}')

    @format.register
    @staticmethod
    def _from_float(arg: float):
        print(f'Вещественное число: {arg}')

    @format.register
    @staticmethod
    def _from_list(arg: list):
        print(f'Элементы списка: {", ".join(map(str, arg))}')

    @format.register
    @staticmethod
    def _from_tuple(arg: tuple):
        print(f'Элементы кортежа: {", ".join(map(str, arg))}')

    @format.register
    @staticmethod
    def _from_dict(arg: dict):
        print(f'Пары словаря: {", ".join(str(item) for item in arg.items())}')

    