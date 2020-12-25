import sys
read = sys.stdin.readline

n = int(read().rstrip())
graph = []

for i in range(n):
    graph.append(list(map(int, read().rstrip().split())))

blue, white = 0, 0
def check(row, col, n, graph):
    global blue, white
    cnt = 0
    for i in range(row, row + n):
        for j in range(col, col + n):
            if graph[i][j] == 1: cnt += 1

    if cnt == n*n: blue += 1
    elif cnt == 0: white += 1
    else:
        check(row, col, n // 2, graph)
        check(row, col + n // 2, n // 2, graph)
        check(row + n // 2, col, n // 2, graph)
        check(row + n // 2, col + n // 2, n // 2, graph)

check(0, 0, n, graph)
print(white)
print(blue)

