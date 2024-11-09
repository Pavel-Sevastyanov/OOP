class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self.default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in self.__dict__:
            return self.__dict__[self._attr]
        elif self.default is None:
            raise AttributeError('Атрибут не найден')
        return self.default

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            self.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')