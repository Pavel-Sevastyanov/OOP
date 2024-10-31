class Peekable:
    def __init__(self, iterable):
        self.it_seq = iterable

    def __iter__(self):
        return self

    def __next__(self):
        self.it_seq = iter(self.it_seq)        
        return next(self.it_seq)

    def peek(self, default='default'):
        self.it_seq = list(self.it_seq)
        if len(self.it_seq) != 0:
            return self.it_seq[0]
        else:
            if default == 'default':
                raise StopIteration
            else:
                return default