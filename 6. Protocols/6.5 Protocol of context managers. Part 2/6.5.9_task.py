from copy import copy, deepcopy

class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.data_copy = deepcopy(self.data) if self.deep else copy(self.data)

    def __enter__(self):
        return self.data_copy

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type != None:
            return True
        else:
            if isinstance(self.data, list):
                self.data[:] = self.data_copy
            elif isinstance(self.data, (set, dict)):
                self.data.clear()
                self.data.update(self.data_copy)
        return False

