class SuperInt(int):
    def repeat(self, n=2):
        result = str(abs(self)) * n
        return SuperInt('-'+ result) if self < 0 else SuperInt(result)

    def to_bin(self):
        result = format(self, 'b')
        return SuperInt(result)

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        yield from (SuperInt(num) for num in str(abs(self)))