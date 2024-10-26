class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)



