import sys
read = sys.stdin.readline

n, k = map(int, read().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
items = [[0,0]]
for i in range(1, n+1):
    w, v = map(int, read().split())
    items.append([w, v])

for i in range(1, n+1): # 물건
    for j in range(1, k+1): # 무게
        if j - items[i][0] < 0: dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]] + items[i][1])

print(dp[n][k])