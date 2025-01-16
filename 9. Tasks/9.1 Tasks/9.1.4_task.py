class ArithmeticProgression:
    def __init__(self, a1, delta):
        self.a1 = a1
        self.delta = delta

    def __iter__(self):
        return self


    def __next__(self):
        elem = self.a1
        self.a1 += self.delta
        return elem


class GeometricProgression:
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q

    def __iter__(self):
        return self

    def __next__(self):
        result = self.b1
        self.b1 *= self.q
        return result
