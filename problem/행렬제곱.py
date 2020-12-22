import sys
read = sys.stdin.readline

n, b = map(int, read().rstrip().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, read().rstrip().split())))

# 행렬 곱셈
def matrix_gob(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += (A[i][k] * B[k][j])
            result[i][j] %= 1000
    return result

# 분할 정복
# 재귀 필요한 곳마다 재귀함수 호출하지말고, 같은 값 반복적으로 사용하는 경우에는 저장해서 사용하기
def divide(b, matrix):
    if b == 1:
        return matrix
    elif b % 2 == 0:
        temp = divide(b//2, matrix)
        return matrix_gob(temp, temp)
    elif b % 2 == 1:
        temp = divide(b//2, matrix)
        return matrix_gob(matrix, matrix_gob(temp, temp))

result = divide(b, matrix)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000, end=' ')
    print()

