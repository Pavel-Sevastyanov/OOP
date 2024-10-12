side = int(input())
matrix = [[1 for j in range(side)] for i in range(side)]

for i in range(side):
    for j in range(side):
        matrix[i][j] = min(i + 1, j + 1, side - i, side - j)

for row in matrix:
    print(*row)
