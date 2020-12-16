import copy
import sys
sys.setrecursionlimit(10**8)

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y, rain):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph_copy[x][y] > rain:
        graph_copy[x][y] = -1
        dfs(x-1, y, rain)
        dfs(x+1, y, rain)
        dfs(x, y-1, rain)
        dfs(x, y+1, rain)
        return True
    return False


result = []
for rain in range(0, max(max(graph))):
    cnt = 0
    graph_copy = copy.deepcopy(graph)

    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain):
                cnt += 1
    result.append(cnt)

print(max(result))