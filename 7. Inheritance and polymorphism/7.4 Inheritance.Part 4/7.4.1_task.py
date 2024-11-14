from collections import UserList

class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        super().__init__(iterable)
        self.iterable = iterable
        self.default = default

    def __getitem__(self, index):
        try:
            return self.iterable[index]
        except:
            return self.default