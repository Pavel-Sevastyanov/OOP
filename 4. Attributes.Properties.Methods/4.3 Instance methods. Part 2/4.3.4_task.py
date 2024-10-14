from math import pi, pow

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * pow(radius, 2)
