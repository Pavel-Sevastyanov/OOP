class Numbers:
    def __init__(self):
        self.set = []
        
    def add_number(self, n):
        self.set.append(n)
        
    def get_even(self):
        return [el for el in self.set if not el % 2]
    
    def get_odd(self):
        return [el for el in self.set if el % 2]