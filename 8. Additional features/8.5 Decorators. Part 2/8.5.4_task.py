def singleton(cls):
    old_new = cls.__new__
    cls._single_obj = None
    
    def new_cls(self, *args, **kwargs): 
        if cls._single_obj is None:
            cls._single_obj = old_new(cls)     
        return cls._single_obj

    cls.__new__ = new_cls
    return cls  