from itertools import cycle

class CyclicList:
    def __init__(self, iterable=None):
        if iterable == None:
            self.start_iterable = []
        else:
            self.start_iterable = list(iterable)
        self.it_iterable = cycle(self.start_iterable)

    def append(self, obj):
        self.start_iterable.append(obj)

    def pop(self, index=-1):
        return self.start_iterable.pop(index)

    def __len__(self):
        return len(self.start_iterable)

    def __getitem__(self, index):
        for elem in range(index):
            next(self.it_iterable)
        result = next(self.it_iterable)
        
        elem = None
        while elem != self.start_iterable[-1]:
            elem = next(self.it_iterable)
        return result