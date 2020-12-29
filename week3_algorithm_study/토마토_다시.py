import sys
from collections import deque
read = sys.stdin.readline

m, n = map(int, read().split())
tomato = []
queue = deque()
fresh = 0
day = 0
for i in range(n):
    tomato.append(list(map(int, read().split())))
    for j in range(m):
        if tomato[i][j] == 0:
            fresh += 1
        elif tomato[i][j] == 1:
            queue.append((j, i))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue and fresh:
    stage = len(queue)
    for _ in range(stage):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny <0 or ny >= n:
                continue
            if tomato[ny][nx] == 0:
                tomato[ny][nx] = 1
                queue.append((nx, ny))
                fresh -= 1
    day += 1

if fresh == 0:
    print(day)
else:
    print(-1)



