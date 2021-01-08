# dfs로 푼다
# 풀이 1
# visited 초깃값 -1로 만들어두고, 1씩 더하면서 갔다가 돌아오면 완성된 경로는 1로 채워진다
# 새로운 경로를 탐색하면서 가다가 1을 만나면 다시 출발점으로 1씩 더하면서 빠꾸한다
# 그럼 출발점에 가능한 경로의 수가 써짐
# dfs 쭉 도는데 dfs 나오면서 이미 지나간 곳이면 그거 갖다쓰는 방식

# import sys
# from collections import deque
# read = sys.stdin.readline
#
# n, m = map(int, read().split())
# jido = []
# for i in range(n):
#     jido.append(list(map(int, read().split())))
#
# visited = [[0 for _ in range(m)] for _ in range(n)]
# def bfs(x, y):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     queue = deque([])
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if jido[nx][ny] >= jido[x][y]:
#                 continue
#             else:
#                 visited[nx][ny] += 1
#                 queue.append((nx, ny))
#     return visited[n-1][m-1]
#
#
#
# print(bfs(0, 0))
# for one in visited:
#     print(one)

# 남의 풀이
import sys
sys.setrecursionlimit(10 ** 8)
read = sys.stdin.readline
N, M = map(int, read().split())
W = [list(map(int, read().split())) for _ in range(N)]
dp = [[-1] * (M) for _ in range(N)]
dp[N - 1][M - 1] = 1

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, W, dp):
    if dp[y][x] != -1:
        return dp[y][x]

    tmp = 0
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < M and 0 <= ny < N and W[y][x] > W[ny][nx]:
            tmp += dfs(nx, ny, W, dp)
    dp[y][x] = tmp

    return dp[y][x]

print(dfs(0, 0, W, dp))

