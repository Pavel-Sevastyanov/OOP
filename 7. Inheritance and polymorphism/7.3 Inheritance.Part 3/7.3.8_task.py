class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        div_x_size = [el % size for el in iterable]
        return super().__new__(cls, div_x_size)