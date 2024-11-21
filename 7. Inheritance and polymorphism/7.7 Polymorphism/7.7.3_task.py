from abc import ABC, abstractmethod

class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.length_row = 0
        self.row = ''
        self.rows = []

    def add(self, string):
        for word in string.split():
            if self.length_row + len(word) - 1 <= self.length:
                self.row += word + ' '
                self.length_row += len(word) + 1
            else:
                self.rows.append(self.row.rstrip())