class Row:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __setattr__(self, name, value):
        if name == 'kwargs':
            object.__setattr__(self, name, value)
        elif name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        elif name in self.kwargs:
            object.__setattr__(self, name, value)
        else:         
            raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        sequence = tuple(f'{k}={repr(v)}' for k, v in self.__dict__.items() if k != "kwargs")
        return f'{self.__class__.__name__}{sequence}'

    def __eq__(self, other):
        if isinstance(other, Row):
            return self.__dict__.items() == other.__dict__.items()
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))