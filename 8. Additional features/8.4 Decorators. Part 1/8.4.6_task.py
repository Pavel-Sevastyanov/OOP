from functools import wraps


class ignore_exception:
    def __init__(self, *args):
        self.exceptions = args

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as error:
                if isinstance(error, self.exceptions):
                    print(f'Исключение {error.__class__.__name__} обработано')
                else:
                    raise error
        return wrapper
