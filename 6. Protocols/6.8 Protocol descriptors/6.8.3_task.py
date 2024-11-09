class MaxCallsException(Exception):
    pass

class LimitedTakes:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, times):
        self.times = times
        self.count = 0

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in self.__dict__:
            self.count += 1
            if self.count <= self.times:
                return self.__dict__[self._attr]
            raise MaxCallsException('Превышено количество доступных обращений')
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        self.__dict__[self._attr] = value