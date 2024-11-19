from collections.abc import Sequence, Sized


class BitArray(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = []
        self.iterable[:] = iterable

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.iterable[index]
        return NotImplemented

    def __len__(self):
        if isinstance(self.iterable, Sized):
            return len(self.iterable)
        return NotImplemented

    def __str__(self):
        return f'{self.iterable}'

    def __invert__(self):
        return BitArray([0 if num else 1 for num in self.iterable])

    def __and__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return BitArray([x and y for x, y in zip(self, other)])
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return BitArray([x or y for x, y in zip(self, other)])
        return NotImplemented


