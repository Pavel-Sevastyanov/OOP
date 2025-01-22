from random import randrange


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.clear_board = [
            [False for col in range(self.cols)]
            for row in range(self.rows)
        ]
        self.plant_mines()
        self.board = [
            [Cell(self, row, col, self.clear_board[row][col])
            for col in range(self.cols)]
            for row in range(self.rows)
        ]
        for row in self.board:
            for cell in row:
                cell.neighbours_mines()

    def plant_mines(self):
        for _ in range(self.mines):
            row, col = randrange(self.rows), randrange(self.cols)
            cell = self.clear_board[row][col]
            while cell:
                row, col = randrange(self.rows), randrange(self.cols)
                cell = self.clear_board[row][col]
            self.clear_board[row][col] = True


class Cell:
    def __init__(self, game, row, col, mine):
        self.row = row
        self.col = col
        self.game = game
        self.mine = mine
        self.neighbours = 0

    def neighbours_mines(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if any([
                    i == 0 and j == 0,
                    self.row == 0 and i == -1,
                    self.row == self.game.rows - 1 and i == 1,
                    self.col == 0 and j == -1,
                    self.col == self.game.cols - 1 and j == 1
                    ]):
                    continue
                
                self.neighbours += self.game.board[self.row + i][self.col + j].mine
