from datetime import time

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return time(*self._transform()).strftime('%H:%M')

    def __add__(self, other):
        if isinstance(other, Time):
            return self.__class__(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            return self
        return NotImplemented

    def transform(self):
        hours = (self.minutes // 60 + self.hours) % 24
        minutes = self.minutes % 60
        return hours, minutes