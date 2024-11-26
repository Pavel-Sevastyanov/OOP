from functools import update_wrapper

class exception_decorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return value, None
        except Exception as error:
            return None, type(error)
