class AdvancedTuple(tuple):
    def __add__(self, other):
        try:
            collect = list(self) + [elem for elem in other]
            return AdvancedTuple(collect)
        except:
            return NotImplemented
        
    def __radd__(self, other):
        try:
            collect = list(other) + [elem for elem in self]
            return AdvancedTuple(collect)
        except:
            return NotImplemented
