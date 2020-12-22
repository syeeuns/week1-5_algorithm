import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
k = int(read())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y = map(int, read().rstrip().split())
    graph[x-1][y-1] = 100 # apple

L = int(read())
direction = {} # 시간에 따른 방향전환을 dict로 저장
for i in range(L):
    a, b = read().rstrip().split()
    direction[int(a)] = b

drow = [1, 0, -1, 0]
dcol = [0, -1, 0, 1]


snake_length = 1
snake = deque([[0,0]])
idx = 3 # 처음엔 오른쪽으로 직진
time = 1
row, col = 0, 0
while True:
    row, col = row + drow[idx], col + dcol[idx]
    if 0 <= row < n and 0 <= col < n and graph[row][col] != 1: # 벽, 몸 안 부딪힌 경우
        # 사과 없는 경우, 머리 가고 꼬리 제거해줌
        # 사과 있는 경우, 머리 가고 꼬리 제거 안함 , 방문표시는 동일
        if graph[row][col] == 0:
            temp = snake.popleft()
            graph[temp[0]][temp[1]] = 0
        graph[row][col] = 1
        snake.append([row, col])
        if time in direction.keys(): # 방향 전환해야하는 시간이 되면 방향 전환
            if direction[time] == 'D':
                idx = (idx + 1) % 4
            elif direction[time] == 'L':
                idx = (idx - 1) % 4
        time += 1
    else:
        print(time)
        break






