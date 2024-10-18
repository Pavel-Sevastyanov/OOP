class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        iter_obj = iter(iterable)
        return cls(next(iter_obj), next(iter_obj), next(iter_obj))

    @classmethod
    def from_str(cls, str):
        coefficients = map(float, str.split())
        return cls(next(coefficients), next(coefficients), next(coefficients))