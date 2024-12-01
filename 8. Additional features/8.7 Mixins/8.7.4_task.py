class ToStringMixin:
    def __repr__(self):
        format_dict = {}
        count = 0
        for k, v in self.__dict__.items():
            format_dict[k] = v
            count += 1
            if count == 6:
                break
        dotes = '' if len(self.__dict__ ) <= 6 else ', ...'
        return f"{self.__class__.__name__}({format_dict}{dotes})"

    