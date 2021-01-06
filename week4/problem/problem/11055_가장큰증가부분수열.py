# dp[i] : i를 마지막 원소로 하는 증가부분 합
import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))

# dp 초기값을 0으로 두면 틀린다