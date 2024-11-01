class SparseArray:
    def __init__(self, default):
        self.default = default
        self.elements = {}

    def __getitem__(self, index):
        return self.elements.get(index, self.default)

    def __setitem__(self, index, value):
        self.elements[index] = value
