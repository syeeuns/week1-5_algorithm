# 가장 마지막 값 들고 있는다
import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))


# 6
# 30 40 10 20 30 50