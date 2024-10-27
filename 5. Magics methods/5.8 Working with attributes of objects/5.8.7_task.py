class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')

