
import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n = int(read())
    sticker = []
    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    for _ in range(2):
        sticker.append(list(map(int, read().split())))
    # dp[0] = [0, sticker[0][0], sticker[1][0]]
    for i in range(n):
        dp[i+1][0] = max(dp[i+1][0], max(dp[i][0], max(dp[i][1], dp[i][2])))
        dp[i+1][1] = max(dp[i+1][1], max(dp[i][0], dp[i][2]) + sticker[0][i])
        dp[i+1][2] = max(dp[i+1][2], max(dp[i][0], dp[i][1]) + sticker[1][i])

    print(max(dp[n]))

