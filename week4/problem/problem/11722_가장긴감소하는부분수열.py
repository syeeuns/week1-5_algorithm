# 새로 나온게 더 작으면 맥스((바로전꺼 +1), 현재값) 갱신
import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
