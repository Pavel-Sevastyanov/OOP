from random import randint

class RandomNumber:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.number = randint(self.start, self.end)

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.cache:
            return self.number
        return randint(self.start, self.end)

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')