class Summator:
    def __init__(self):
        self.m = 1

    def total(self, n):
        return sum(i ** self.m for i in range(1, n + 1))


class SquareSummator(Summator):
    def __init__(self):
        self.m = 2


class QubeSummator(Summator):
    def __init__(self):
        self.m = 3


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m
