from abc import ABC, abstractmethod

class Stat(ABC):
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)

    def add(self, num):
        self.iterable.append(num)

    @abstractmethod
    def result(self):
        pass

    def clear(self):
        self.iterable.clear()


class MinStat(Stat):
    def result(self):
        return min(self.iterable, default=None)

class MaxStat(Stat):
    def result(self):
        return max(self.iterable, default=None)

class AverageStat(Stat):
    def result(self):
        return (sum(self.iterable) / len(self.iterable)) if self.iterable else None

