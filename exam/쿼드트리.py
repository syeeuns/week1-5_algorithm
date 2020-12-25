import sys
read = sys.stdin.readline

n = int(read())
graph = []
for i in range(n):
    graph.append(list(map(int, read().rstrip())))

result = []

# 분할을 시작한다 -> 괄호를 연다
# 분할이 끝났다 -> 괄호를 닫는다
# 분할 중 -> 그냥 숫자만 추가한다
def check(row, col, n, graph):
    cnt = 0
    for i in range(row, row + n):
        for j in range(col, col + n):
            if graph[i][j] == 1:
                cnt += 1
    if cnt == n*n:
        result.append('1')
    elif cnt == 0:
        result.append('0')
    else:
        result.append('(')
        check(row, col, n // 2, graph)
        check(row, col+n//2, n // 2, graph)
        check(row+n//2, col, n // 2, graph)
        check(row+n//2, col+n//2, n // 2, graph)
        result.append(')')

check(0, 0, n, graph)
print(''.join(result))
