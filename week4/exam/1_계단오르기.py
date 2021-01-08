import sys
read = sys.stdin.readline

n = int(read())
dp = [[0 for _ in range(3)] for _ in range(n+1)]
stair = [0]
for _ in range(n):
    stair.append(int(read()))

dp[1][1] = stair[1]
for i in range(2, n+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stair[i]
    dp[i][2] = dp[i-1][1] + stair[i]

print(max(dp[n]))