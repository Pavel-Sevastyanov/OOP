class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y, self.color}'

    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)

    def __neg__(self):
        return self.__class__(-self.x, -self.y, self.color)

    def __invert__(self):
        self.inv_color = tuple(255 - i for i in self.color)
        return self.__class__(self.y, self.x, self.inv_color)