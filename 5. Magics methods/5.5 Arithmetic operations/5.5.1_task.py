class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"{self.__class__.__name__}{self.proteins, self.fats, self.carbohydrates}"

    def __add__(self, other):
        if isinstance(other, FoodInfo):       
            return self.__class__(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented    
        
    def __mul__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return self.__class__(self.proteins * n, self.fats * n, self.carbohydrates * n)
        return NotImplemented        
    
    def __truediv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return self.__class__(self.proteins / n, self.fats / n, self.carbohydrates / n)        
        return NotImplemented
         
    def __floordiv__(self, n):
        if isinstance(n, int) or isinstance(n, float):
            return self.__class__(self.proteins // n, self.fats // n, self.carbohydrates // n)
        return NotImplemented        