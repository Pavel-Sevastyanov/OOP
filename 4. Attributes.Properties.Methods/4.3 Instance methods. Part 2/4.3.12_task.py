class Todo:
    def __init__(self):
        self.things = []
        
    def add(self, task, priority):
        self.things.append((task, priority))
        
    def get_by_priority(self, n):
        return [el[0] for el in self.things if el[1] == n]
    
    def get_low_priority(self):
        low = min(self.things, key=lambda el: el[1], default=(None, None))[1]
        return [el[0] for el in self.things if el[1] == low]         

    def get_high_priority(self):
        high = max(self.things, key=lambda el: el[1], default=(None, None))[1]
        return [el[0] for el in self.things if el[1] == high]  