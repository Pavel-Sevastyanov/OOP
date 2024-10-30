class AttrsIterator:
    def __init__(self, obj):
        self.obj_attrs = list(obj.__dict__.items())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i != len(self.obj_attrs):
            element = self.obj_attrs[self.i]           
            self.i += 1
            return element
        raise StopIteration