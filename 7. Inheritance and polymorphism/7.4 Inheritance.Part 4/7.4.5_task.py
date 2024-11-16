from collections import UserList

class NumberList(UserList):
    def __init__(self, iterable=()):
        self.error = TypeError('Элементами экземпляра класса NumberList должны быть числа')
        for elem in iterable:
            if not isinstance(elem, (int, float)):
                raise self.error
        super().__init__(iterable)
    
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise self.error
        self.data[index] = value

    def __add__(self, other):
        if not hasattr(other, '__iter__'):
            return NotImplemented
        for elem in other:
            if not isinstance(elem, (int, float)):
                raise self.error
        return self.data.__add__(list(other))

    def __iadd__(self, other):
        if not hasattr(other, '__iter__'):
            return NotImplemented
        for elem in other:
            if not isinstance(elem, (int, float)):
                raise self.error
        return self.data.__iadd__(list(other))

    def append(self, elem):
        if not isinstance(elem, (int, float)):
            raise self.error       
        return self.data.append(elem)

    def extend(self, other):
        if not hasattr(other, '__iter__'):
            return NotImplemented
        for elem in other:
            if not isinstance(elem, (int, float)):
                raise self.error    
        return self.data.extend(list(other))

    def insert(self, index, elem):
        if not isinstance(elem, (int, float)):
            raise self.error      
        return self.data.insert(index, elem)