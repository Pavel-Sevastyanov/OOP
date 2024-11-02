from copy import deepcopy

class PermaDict:
    def __init__(self, data=None):
        if data is None:
            self.sequences = {}
        else:
            self.sequences = deepcopy(data)

    def keys(self):
        return self.sequences.keys()

    def values(self):
        return self.sequences.values()

    def items(self):
        return self.sequences.items()
    
    def __len__(self):
        return len(self.sequences)

    def __iter__(self):
        yield from self.sequences

    def __getitem__(self, key):
        return self.sequences[key]

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('Изменение значения по ключу невозможно')
        self.sequences[key] = value

    def __delitem__(self, key):
        if key in self:
            del self.sequences[key]
            