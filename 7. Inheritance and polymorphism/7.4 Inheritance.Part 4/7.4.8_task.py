from collections import UserString

class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index, value):
        changed_string = ''
        start, end = (0, len(self.data)) if index >= 0 else (-len(self.data), 0)

        for i in range(start, end):
            if i == index:
                changed_string += value
                continue
            changed_string += self.data[i]           
        self.data = changed_string

    def __delitem__(self, index):
        changed_string = ''
        start, end = (0, len(self.data)) if index >= 0 else (-len(self.data), 0)

        for i in range(start, end):
            if i == index:
                continue
            changed_string += self.data[i]           
        self.data = changed_string

