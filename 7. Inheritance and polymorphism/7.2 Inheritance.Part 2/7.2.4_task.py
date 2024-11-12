class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, num=1):
        self.value += num

    def dec(self, num=1):
        self.value = max(self.value - num, 0)

    
class DoubledCounter(Counter):
    def inc(self, num=1):
        super().inc(num * 2)

    def dec(self, num=1):
        super().dec(num * 2)