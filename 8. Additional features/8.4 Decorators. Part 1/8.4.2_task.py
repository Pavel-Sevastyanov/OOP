from functools import wraps

class limited_calls:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            self.count += 1
            if self.count > self.n:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            return func(*args, **kwargs)

        return wrapper