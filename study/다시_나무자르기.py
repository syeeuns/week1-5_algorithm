import sys
read = sys.stdin.readline

n, m = map(int, read().rstrip().split())
trees = sorted(list(map(int, read().rstrip().split())))

# 10 15 17 20
# m > remain -> 덜 잘라야 함
# m < remain -> 더 잘라야 함
start = 0
end = trees[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    remain = 0
    for one in trees:
        if one > mid:
            remain += one - mid
    if remain == m:
        answer = mid
        break
    elif remain < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)

