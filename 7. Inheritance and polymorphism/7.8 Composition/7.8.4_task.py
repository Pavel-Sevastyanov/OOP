from collections import OrderedDict

class Queue:
    def __init__(self, pairs={}):
        self.pairs = OrderedDict(pairs)

    def add(self, elem):
        if elem[0] in self.pairs:
            del self.pairs[elem[0]]
        self.pairs[elem[0]] = elem[1]

    def pop(self):
        if not self.pairs:
            raise KeyError('Очередь пуста')
        return self.pairs.popitem(last=False)

    def __repr__(self):
        return f'Queue({[pair for pair in self.pairs.items()]})'

    def __len__(self):
        return len(self.pairs)