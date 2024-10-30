class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.step = n + 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        element = self.iterable[self.index]
        self.index += self.step
        return element