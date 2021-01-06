import sys
read = sys.stdin.readline

t = int(read())
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(t):
    n = int(read())
    if n <= 3: print(dp[n])
    else:
        for j in range(4, n+1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])
