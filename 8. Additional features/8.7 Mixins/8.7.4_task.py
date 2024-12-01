class ToStringMixin:
    def __repr__(self):
        format_dict = [f'{repr(k)}: {repr(v)}' for k, v in self.__dict__.items()]
        if len(self.__dict__) > 6:
            format_dict = format_dict[:6] + ['...']
        return f"{self.__class__.__name__}(\u007b{', '.join(format_dict)}\u007d)"

    