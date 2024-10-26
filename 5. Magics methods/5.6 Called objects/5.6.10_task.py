class SortKey:
    def __init__(self, *args):
        self.__dict__ = {k: k for k in args}

    def __call__(self, arg):       
        return tuple(getattr(arg, attr) for attr in self.__dict__)