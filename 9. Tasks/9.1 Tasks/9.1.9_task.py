class TicTacToe:
    def __init__(self):
        self.table = [[' ' for _ in range(3)] for _ in range(3)]
        self.marker = 'X'
        self.winner_game = None
        self.count = 0

    def mark(self, row, col):
        if self.winner_game:
            print('Игра окончена')
        elif self.table[row - 1][col - 1] == ' ':
            self.table[row - 1][col - 1] = self.marker
            self.count += 1
            if self.count >= 5:
                self.winner()
            self.marker = 'O' if self.marker == 'X' else 'X'
        else:
            print('Недоступная клетка')

    def winner(self):
        diagonal, reverse_diagonal = '', ''
        for i in range(3):
            diagonal += self.table[i][i]
            reverse_diagonal += self.table[-i][-i]
            row, col = '', ''
            for j in range(3):
                row += self.table[i][j]
                col += self.table[j][i]
            if self.__class__.check(row):
                self.winner_game = row[0]
                return self.winner_game
            elif self.__class__.check(col):
                self.winner_game = col[0]
                return self.winner_game
        if self.__class__.check(diagonal):
            self.winner_game = diagonal[0]
        elif self.__class__.check(reverse_diagonal):
            self.winner_game = reverse_diagonal[0]
        if self.count == 9 and not self.winner_game:
            self.winner_game = 'Ничья'
        return self.winner_game

    def show(self):
        table = ['|'.join(row) for row in self.table]
        print('\n-----\n'.join(table))

    @staticmethod
    def check(line):
        return ' ' not in line and len(set(line)) == 1
