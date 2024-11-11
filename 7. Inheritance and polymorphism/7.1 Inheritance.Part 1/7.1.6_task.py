class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, num=1):
        self.value += num

    def dec(self, num=1):
        if self.value - num >= 0:
            self.value -= num
        else:
            self.value = 0

class NonDecCounter(Counter):
    def dec(self, num=1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.start = start
        self.value = self.start
        self.limit = limit

    def inc(self, num=1):
        if self.value + num <= self.limit:
            self.value += num
        else:
            self.value = self.limit