import sys
read = sys.stdin.readline

n = int(read().rstrip())
target = sorted(list(map(int, read().rstrip().split())))
m = int(read().rstrip())
my = list(map(int, read().rstrip().split()))
answer = [0 for _ in range(m)]


for i in range(len(my)):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target[mid] == my[i]:
            answer[i] = 1
            break
        elif target[mid] < my[i]:
            start = mid + 1
        else:
            end = mid - 1
    print(answer[i])


