from functools import update_wrapper
from itertools import chain

class takes_numbers:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for arg in chain(args, kwargs.values()):
            if not isinstance(arg, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)