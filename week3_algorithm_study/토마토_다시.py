# 잘 푼 풀이 참고해서 다시 품

# 한 줄씩 입력 받으면서 안 익은 토마토 개수 확인
# 토마토 익어갈때마다 안 익은 토마토 -= 1 해줌
# 그러면 마지막에 0인거 있나없나 for문 돌면서 확인 안해도 됨
# while문 한번 돌때마다 queue 길이만큼 돌아서 날짜 체크

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



