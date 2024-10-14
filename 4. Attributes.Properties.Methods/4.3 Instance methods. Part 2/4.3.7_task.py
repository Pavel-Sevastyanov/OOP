from itertools import cycle

class Gun:
    def __init__(self):
        self.sound = cycle(['pif', 'paf'])
        self.shots = 0

    def shoot(self):
        self.shots += 1
        print(next(self.sound))

    def shots_count(self):
        return self.shots

    def shots_reset(self):
        self.shots = 0
        self.sound = cycle(['pif', 'paf'])