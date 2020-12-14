import time

n = input()
start_time = time.time()

alphabet = ['a','b','c','d','e','f','g','h']
number = ['1','2','3','4','5','6','7','8']
start = [n[0], int(n[1])-1]

for i in range(len(alphabet)):
    if n[0] == alphabet[i]:
        start[0] = int(number[i]) -1

start_x = start[0]
start_y = start[1]
dx = [-2, -1, -2, -1, 2, 1, 2, 1]
dy = [-1, -2, 1, 2, -1, -2, 1, 2]

arr = [[0 for _ in range(8)] for _ in range(8)]

cnt = 0
for i in range(8):
    nx = start_x + dx[i]
    ny = start_y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

end_time = time.time()
print('time : ', end_time - start_time)
print(cnt)