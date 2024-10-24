class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.__class__(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return self.__class__(self.x * n, self.y * n)
        return NotImplemented        

    def __rmul__(self, n):
        return self.__mul__(n)       

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return self.__class__(self.x / n, self.y / n)
        return NotImplemented        