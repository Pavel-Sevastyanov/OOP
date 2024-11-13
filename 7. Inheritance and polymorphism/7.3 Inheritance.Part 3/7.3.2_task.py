class LowerString(str):
    def __new__(cls, obj=''):
        low_str = super().__new__(cls, obj)
        if low_str:
            return str(low_str).lower()
        return low_str
