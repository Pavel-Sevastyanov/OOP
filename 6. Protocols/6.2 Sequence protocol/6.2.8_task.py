class MutableString:
    def __init__(self, string=''):
        self.string = list(string)

    def lower(self):
        self.string = ''.join(map(str.lower, self.string))

    def upper(self):
        self.string = ''.join(map(str.upper, self.string))

    def __str__(self):
        return ''.join(self.string)

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(''.join(self.string))})"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        yield from self.string

    def __getitem__(self, index):
        if isinstance(index, slice):
            return MutableString(''.join(self.string)[index])
        return MutableString(''.join(self.string)[index])

    def __setitem__(self, index, value):       
        if isinstance(index, slice):
            self.string[index] = value
        elif isinstance(index, int):
            self.string[index] = value
        self.string = ''.join(self.string)
        self.string = list(self.string)

    def __delitem__(self, index):
        if isinstance(index, slice):
            del self.string[index]
        else:
            del self.string[index]

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(''.join(self.string + other.string))
        return NotImplemented