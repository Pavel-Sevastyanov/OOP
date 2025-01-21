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
            if self.__class__.check(row, col):
                self.winner_game = self.table[i][i]
                return self.winner_game
        if self.__class__.check(diagonal, reverse_diagonal):
            self.winner_game = self.table[1][1]
        if self.count == 9 and not self.winner_game:
            self.winner_game = 'Ничья'
        return self.winner_game

    def show(self):
        table = ['|'.join(row) for row in self.table]
        print('\n-----\n'.join(table))

    @staticmethod
    def check(line1, line2):
        result = any([line1 in ('XXX', 'OOO'), line2 in ('XXX', 'OOO')])
        return result
