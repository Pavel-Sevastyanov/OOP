class AdvancedList(list):
    def join(self, delimiter=' '):
        return delimiter.join(str(elem) for elem in self)

    def map(self, func):
        self[:] = [func(elem) for elem in self]

    def filter(self, func):
        self[:] = [elem for elem in self if func(elem)]



