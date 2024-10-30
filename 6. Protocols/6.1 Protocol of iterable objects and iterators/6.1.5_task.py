from itertools import chain

class RandomLooper:
    def __init__(self, *args):
        self.objects = chain(*args)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.objects)