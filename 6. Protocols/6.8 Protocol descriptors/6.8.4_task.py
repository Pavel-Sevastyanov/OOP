class TypeChecked:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, *args):
        self.types = args

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if not self._attr in self.__dict__:
            raise AttributeError('Атрибут не найден')
        return self.__dict__[self._attr]

    def __set__(self, obj, value):
        if not isinstance(value, self.types):
            raise TypeError('Некорректное значение')
        self.__dict__[self._attr] = value