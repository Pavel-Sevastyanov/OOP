from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def validate(self, obj):
        pass

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self.validate(value):
            obj.__dict__[self._attr] = value

    def __delete__(self, obj):
        del obj.__dict__[self._attr]


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if not isinstance(obj, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if not self.minvalue is None:
            if obj < self.minvalue:
                raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if not self.maxvalue is None:   
            if obj > self.maxvalue:
                raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if not self.minsize is None:
            if len(obj) < self.minsize:
                raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if not self.maxsize is None:   
            if len(obj) > self.maxsize:
                raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if not self.predicate is None: 
            if not self.predicate(obj):
                raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True