from enum import Enum

class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, lang):
        seasons = {
            1: ('winter', 'зима'), 
            2: ('spring', 'весна'), 
            3: ('summer', 'лето'),
            4: ('fall', 'осень')
            }
        if lang == 'en':
            return seasons[self.value][0]
        return seasons[self.value][1]
