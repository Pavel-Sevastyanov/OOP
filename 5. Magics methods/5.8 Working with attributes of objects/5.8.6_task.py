class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 0
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        
    def __setattr__(self, name, value):
        result = name not in self.__dict__
        object.__setattr__(self, name, value)
        self.__dict__['attrs_num'] += result

    def __delattr__(self, name):
        object.__delattr__(self, name)
        self.__dict__['attrs_num'] -= 1        