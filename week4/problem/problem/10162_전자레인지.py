import sys
read = sys.stdin.readline

n = int(read())
time = [300, 60, 10]
answer = [0,0,0]
while n > 0:
    if n >= 300:
        answer[0] += n // 300
        n %= 300
    elif n >= 60:
        answer[1] += n // 60
        n %= 60
    elif n >= 10:
        answer[2] += n // 10
        n %= 10
    else:
        print(-1)
        exit()

print(*answer)
