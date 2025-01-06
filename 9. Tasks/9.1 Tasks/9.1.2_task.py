from math import sqrt


class Vector:
    def __init__(self, *args):
        self.coordinates = args

    
    def __str__(self):
        return f'{self.coordinates}'

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, self.__class__):
            return Vector(*map(lambda x, y: x + y, self.coordinates, other.coordinates))
        return NotImplemented

    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, self.__class__):
            return Vector(*map(lambda x, y: x - y, self.coordinates, other.coordinates))
        return NotImplemented

    def __mul__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, self.__class__):
            return sum(map(lambda x, y: x * y, self.coordinates, other.coordinates))
        return NotImplemented

    def norm(self):
        return sqrt(sum(i ** 2 for i in self.coordinates))

    def __eq__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, self.__class__):
            return self.coordinates == other.coordinates
        return NotImplemented
