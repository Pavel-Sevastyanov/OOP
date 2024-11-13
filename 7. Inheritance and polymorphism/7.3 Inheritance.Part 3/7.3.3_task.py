class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return super().__str__().lower() == other.lower()
        return NotImplemented
    
    def __ne__(self, other): 
        if isinstance(other, (str, FuzzyString)):
            return super().__str__().lower() != other.lower()
        return NotImplemented    

    def __lt__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return super().__str__().lower() < other.lower()
        return NotImplemented
        
    def __gt__(self, other): 
        if isinstance(other, (str, FuzzyString)):
            return super().__str__().lower() > other.lower()
        return NotImplemented

    def __le__(self, other): 
        if isinstance(other, (str, FuzzyString)):
            return super().__str__().lower() <= other.lower()
        return NotImplemented

    def __ge__(self, other): 
        if isinstance(other, (str, FuzzyString)):
            return super().__str__().lower() >= other.lower()
        return NotImplemented

    def __contains__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return other.lower() in super().__str__().lower()
        return NotImplemented 