from keyword import kwlist

class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        else:
            try:
                return obj.__dict__[self._attr]
            except:
                raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value