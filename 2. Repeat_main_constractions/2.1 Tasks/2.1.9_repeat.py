import re

def is_integer(string):    
    result = re.fullmatch(r'-?\d+', string)
    return bool(result)