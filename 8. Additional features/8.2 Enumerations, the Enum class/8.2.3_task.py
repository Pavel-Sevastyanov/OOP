from enum import Enum
from datetime import date, timedelta

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, considering_today=False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today
        self.day_until = (self.weekday.value - self.today.weekday()) % 7

    def date(self):
        if self.today.weekday() == self.weekday.value and self.considering_today:
            return self.today
        else:
            self.day_until = self.day_until if self.day_until != 0 else 7
        return self.today + timedelta(days = self.day_until)

    def days_until(self):            
        return self.day_until