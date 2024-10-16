class HourClock:
    def __init__(self, hours):
        self.hours = hours
        
    def get_time(self):
        return self._hours
    
    def set_time(self, hours):
        if not (isinstance(hours, int) and 1 <= hours <= 12):
            raise ValueError('Некорректное время')
        else:
            self._hours = hours

    hours = property(get_time, set_time)