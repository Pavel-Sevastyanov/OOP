import re

def is_decimal(string):    
    result = re.fullmatch(r'(-?\d*\.?\d+)|(-?\d+\.?\d*)', string)
    return bool(result)
