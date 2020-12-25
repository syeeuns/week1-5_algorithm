n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))

visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if ice[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)