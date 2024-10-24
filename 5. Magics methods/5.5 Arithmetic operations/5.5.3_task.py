class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return self.__class__(self.string + other.string)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return self.__class__(self.string * n)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __truediv__(self, n):
        if isinstance(n, int):
            return self.__class__(self.string[:len(self.string) // n])
        return NotImplemented

    def __lshift__(self, n):
        if isinstance(n, int):
            if not n:
                return self.__class__(self.string)
            return self.__class__(self.string[:-n]) if n < len(self.string) else self.__class__('')
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if not n:
                return self.__class__(self.string)            
            return self.__class__(self.string[n:]) if n < len(self.string) else self.__class__('')
        return NotImplemented
