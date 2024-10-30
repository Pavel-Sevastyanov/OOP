class Point:
    def __init__(self, x, y, z):
        self.it_obj = (x, y, z)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.it_obj}'

    def __iter__(self):
        yield from self.it_obj
        