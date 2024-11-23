class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = self.convert_min(start_time)
        self.duration = self.convert_min(duration)
        self.end_time = self.start_time + self.duration
        
    @staticmethod    
    def convert_min(time):
        hours, minute = map(int, time.split(':'))
        return hours * 60 + minute
        
    def __str__(self):
        return f'{self.topic},({self.start_time//60:02}:{self.start_time%60:02}), ({self.end_time//60:02}:{self.end_time%60:02})'
            
class Conference:
    def __init__(self):
        self.conf = []
        
    def add(self, event: Lecture):
        if self.conf:
            for existing_lecture in self.conf:
                if (event.start_time < existing_lecture.start_time + existing_lecture.duration 
                and 
                existing_lecture.start_time < event.start_time + event.duration
                ):
                    raise ValueError ('Провести выступление в это время невозможно')
        self.conf.append(event)
        self.conf.sort(key = lambda x: x.start_time)
   
            
    def longest_lecture(self):
        max_lec = max(self.conf, key = lambda x: x.duration)
        return f'{max_lec.duration//60:02}:{max_lec.duration%60:02}'
        
    def longest_break(self):
        res = []
        for index, event in enumerate(self.conf[:-1]):
            next = self.conf[index +1]
            res+=[next.start_time - event.end_time]
        br = max(res, 0)
        return f'{br//60:02}:{br%60:02}'
        
    def total(self):
        total = sum([event.duration for event in self.conf])
        return f'{total//60:02}:{total%60:02}'
        
    def __iter__(self):
        return iter(self.conf)