class LoopTracker:
    def __init__(self, iterable):
        self._iterable = list(iterable)
        self._it_seq = iter(self._iterable)
        self._accesses = 0
        self._empty_accesses = 0
        self._last = ''

    def __iter__(self):
        return self

    def __next__(self):
        try:
            elem = next(self._it_seq)
            self._last = elem
            self._accesses += 1
            return elem
        except StopIteration:
            self._empty_accesses += 1
            raise StopIteration

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses
    
    @property
    def first(self):
        if len(self._iterable) == 0:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self._iterable[0]
    
    @property
    def last(self):
        if self._last == '':
            raise AttributeError('Последнего элемента нет')
        return self._last

    def is_empty(self):
        if not self._iterable or self._last == self._iterable[-1]:
            return True
        return False