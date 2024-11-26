from functools import wraps

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for a, t in zip(args, self.types):
                if not isinstance(a, t):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper