import sys
read = sys.stdin.readline

n = int(read())
stick = []
for i in range(n):
    stick.append(int(read()))

# 뒤에서부터 max값 갱신하면서 max보다 크면 보임
cnt = 1
max = stick[-1]
for i in range(n-2, -1, -1):
    if max < stick[i]:
        max = stick[i]
        cnt += 1

print(cnt)

