from collections import UserDict

class EasyDict(UserDict):
    def __getattr__(self, key):
        value = self.data.__getitem__(key)
        return value
