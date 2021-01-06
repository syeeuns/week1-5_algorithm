import sys
read = sys.stdin.readline

n = int(read())
panic = sorted(list(map(int, read().split())))
cnt = 0
temp = 0
for i in range(len(panic)):
    temp += 1
    if panic[i] <= temp:
        cnt += 1
        temp = 0

print(cnt)