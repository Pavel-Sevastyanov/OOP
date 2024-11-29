def snake_case(attrs=False):
    def decorator(cls):
        elems = {k: v for k, v in cls.__dict__.items()}
        for elem, v in elems.items():
            if not elem.startswith('__'):
                new_name = [
                    '_' + c.lower() if c.isupper()
                    else c.lower()
                    for c in elem
                ]
                new_name = ''.join(new_name).lstrip('_')
                if elem.startswith('_'):
                    new_name = '_' + ''.join(new_name)
                if hasattr(cls, elem) and attrs or callable(v):
                    delattr(cls, elem)
                    setattr(cls, new_name, v)
        return cls

    return decorator