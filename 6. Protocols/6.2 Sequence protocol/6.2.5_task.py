from copy import deepcopy

class OrderedSet:
    def __init__(self, iterable=None):
        if iterable is None:
            self.elements = {}
        else:
            self.elements = dict.fromkeys(deepcopy(iterable))

    def add(self, obj):
        self.elements[obj] = None
    
    def discard(self, obj):
        if obj in self:
            del self.elements[obj]
    
    def __len__(self):
        return len(self.elements)

    def __contains__(self, obj):
        return obj in self.elements

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.elements) == tuple(other.elements)
        elif isinstance(other, set):
            return set(self.elements) == other
        return NotImplemented

    def __iter__(self):
        yield from self.elements