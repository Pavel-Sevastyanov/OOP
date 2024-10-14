class Scales:
    def __init__(self):
        self.right_bowl = 0
        self.left_bowl = 0

    def add_right(self, mass):
        self.right_bowl += mass
        
    def add_left(self, mass):
        self.left_bowl += mass

    def get_result(self):
        if self.right_bowl > self.left_bowl:
            return 'Правая чаша тяжелее'
        elif self.right_bowl < self.left_bowl:
            return 'Левая чаша тяжелее'
        return 'Весы в равновесии'