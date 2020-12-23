import sys
read = sys.stdin.readline

n = int(read().rstrip())
sol = sorted(list(map(int, read().rstrip().split())))

left, right = 0, n - 1
best_sum = 2000000001
best_front, best_back = 0, 0
while left < right:
    now_sum = sol[left] + sol[right]
    if abs(now_sum) < best_sum:
        best_sum = abs(now_sum)
        best_front, best_back = sol[left], sol[right]
    if now_sum == 0:
        break
    elif now_sum < 0:
        left += 1
    else:
        right -= 1
print(best_front, best_back)