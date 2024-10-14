from itertools import cycle

class Gun:
    def __init__(self):
        self.sound = cycle(['pif', 'paf'])

    def shoot(self):
        print(next(self.sound))
