def get_method_owner(cls, method):
    for obj in cls.mro():
        if method in obj.__dict__:
            return obj