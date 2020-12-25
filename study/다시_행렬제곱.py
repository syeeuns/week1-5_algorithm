import sys
read = sys.stdin.readline

n, b = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(n)]

def matrix_calculate(a, b):
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new[i][j] += a[i][k] * b[k][j]
            new[i][j] %= 1000
    return new

def divide(b, matrix):
    if b == 1:
        return matrix
    elif b % 2 == 0:
        temp = divide(b//2, matrix)
        return matrix_calculate(temp, temp)
    elif b % 2 == 1:
        temp = divide(b-1, matrix)
        return matrix_calculate(temp, matrix)

result = divide(b, matrix)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000, end=' ')
    print()
