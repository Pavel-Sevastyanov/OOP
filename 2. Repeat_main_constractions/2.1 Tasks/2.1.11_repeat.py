import re

def is_fraction(string):    
    result = re.fullmatch(r'(-?\d+/[1-9]\d*)|(-?\d+/0+[1-9]\d*)', string)
    return bool(result)