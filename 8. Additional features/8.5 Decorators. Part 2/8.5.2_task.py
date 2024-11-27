def add_attr_to_class(**kwargs):
    def decorator(cls):
        for k, v in kwargs.items():
            setattr(cls, k, v)
        return cls
    return decorator