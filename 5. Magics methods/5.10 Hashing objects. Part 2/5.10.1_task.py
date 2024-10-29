class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @property
    def _fields(self):
        return self._x, self._y, self._color

    def __repr__(self):
        return f'{self.__class__.__name__}{self._x, self._y, self._color}'
    
    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._fields == other._fields
        return NotImplemented
    
    def __hash__(self):
        return hash(self._fields)  

dote = ColoredPoint(1, 2, 'yellow')
print(dote.x)
            