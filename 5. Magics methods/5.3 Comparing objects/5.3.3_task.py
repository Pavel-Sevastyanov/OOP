from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __repr__(self):
        return f"Month{self.year, self.month}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple) and len(other) == 2:
            return self.year == other[0] and self.month == other[1]
        return NotImplemented
      
    def __lt__(self, other):
        if isinstance(other, Month):
            if self.year < other.year:
                return True
            elif self.year == other.year:
                return self.month < other.month 
        elif isinstance(other, tuple) and len(other) == 2:
            if self.year < other[0]:
                return True
            elif self.year == other[0]:
                return self.month < other[1]
        return NotImplemented