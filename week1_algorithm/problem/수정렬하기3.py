import sys

counting = [0] * 10001
for _ in range(int(sys.stdin.readline().rstrip())):
    counting[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(counting)):
    if counting[i] == 0:
        continue
    else:
        for j in range(counting[i]):
            print(i)