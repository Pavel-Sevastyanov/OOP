import sys

def check_coord(coords):
    coords = map(float, coords)
    return -90 <= next(coords) <= 90 and -180 <= next(coords) <= 180

print(*(check_coord(eval(el.strip())) for el in sys.stdin), sep='\n')