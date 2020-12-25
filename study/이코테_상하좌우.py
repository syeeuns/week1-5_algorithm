n = int(input())
direction = list(input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move_types = ['R', 'L', 'D', 'U']

arr = [[i for i in range(n)] for j in range(n)]
current_x = 0
current_y = 0
for i in direction:
    for j in range(len(move_types)):
        if i == move_types[j]:
            current_x += dx[j]
            current_y += dy[j]
            if not(0 <= current_x < n) or not(0 <= current_y < n):
                current_x -= dx[j]
                current_y -= dy[j]


print(current_x+1, current_y+1)