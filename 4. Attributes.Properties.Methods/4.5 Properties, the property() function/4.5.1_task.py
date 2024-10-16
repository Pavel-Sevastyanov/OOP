class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimiter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimiter)
    area = property(get_area)

