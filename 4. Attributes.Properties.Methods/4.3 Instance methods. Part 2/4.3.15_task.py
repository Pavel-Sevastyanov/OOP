class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.alphabet = [chr(i) for i in range(ord('a'), ord('a') + 8)]

    def get_char(self):
        return 'N'

    def can_move(self, x, y):
        x1 = self.alphabet.index(self.horizontal)
        x2 = self.alphabet.index(x)
        difference = (x1 - x2) * (self.vertical - y)
        return True if difference == 2 or difference == -2 else False

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        row = 8 - self.vertical
        col = self.alphabet.index(self.horizontal) 
        chess_board = [['.' for j in range(8)] for i in range(8)]
        chess_board[row][col] = 'N'
        for i in range(8):
            for j in range(8):
                if (row - i) * (col - j) == 2 or (row - i) * (col - j) == -2:
                    chess_board[i][j] = "*"
        for i in chess_board:
            print(*i, sep='')