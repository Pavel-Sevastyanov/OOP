from abc import ABC, abstractmethod

class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.length_row = 0
        self.row = ''
        self.rows = []

    def add(self, string):
        for word in string.split():
            if self.length_row + len(word) <= self.length:
                self.row += word + ' '
                self.length_row += len(word) + 1
            else:
                self.rows.append(self.row.rstrip())
                self.row = word + ' '
                self.length_row = len(word) + 1

    @abstractmethod
    def end(self):
        pass

class LeftParagraph(Paragraph):
    def end(self):
        self.rows.append(self.row.rstrip())
        for row in self.rows:
            print(row)
        self.rows = []
        self.row = ''
        self.length_row = 0

class RightParagraph(Paragraph):
    def end(self):
        self.rows.append(self.row.rstrip())
        for row in self.rows:
            space = self.length - len(row)
            print(f'{space * " "}{row}')
        self.rows = []
        self.row = ''
        self.length_row = 0      