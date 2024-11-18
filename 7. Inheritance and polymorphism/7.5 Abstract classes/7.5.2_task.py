from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
        self.alphabet = [chr(i) for i in range(ord('a'), ord('a') + 8)]
    
    @abstractmethod
    def can_move(self):
        pass

class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        x1 = self.alphabet.index(self.horizontal)
        x2 = self.alphabet.index(horizontal)
        return (
    x2 == x1 + 1 
    or x2 == x1 - 1 
    or x2 == x1
    ) and (
        vertical == self.vertical + 1 
        or vertical == self.vertical - 1 
        or vertical == self.vertical
        ) and not (
            x2 == x1 
            and vertical == self.vertical
            )

class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        x1 = self.alphabet.index(self.horizontal)
        x2 = self.alphabet.index(horizontal)
        difference = (x1 - x2) * (self.vertical - vertical)
        return bool(difference == 2 or difference == -2)
