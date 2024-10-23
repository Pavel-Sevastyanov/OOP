class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value for j in range(self.cols)] for i in range(self.rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __str__(self):
        matrix_string = '\n'.join([' '.join(map(str, row)) for row in self.matrix])
        return matrix_string

    def __repr__(self):
        return f"{self.__class__.__name__}{self.rows, self.cols}"

    def __pos__(self):
        return self.__class__(self.rows, self.cols, self.value)

    def __neg__(self):
        new_matrix = self.__class__(self.rows, self.cols)
        new_matrix.matrix = [[-el for el in row] for row in self.matrix]
        return new_matrix

    def __invert__(self):
        new_matrix = self.__class__(self.cols, self.rows)
        new_matrix.matrix = [*zip(*self.matrix)]
        return new_matrix

    def __round__(self, num=None):
        new_matrix = self.__class__(self.rows, self.cols)
        new_matrix.matrix = [[round(el, num) for el in row] for row in self.matrix]
        return new_matrix