# 양옆의 집과 색이 달라야 한다
# 그럼 R G R 같은건 가능하겠네
# 각 집을 알쥐비로 칠하는 비용이 한 줄씩 주어진다
import sys
read = sys.stdin.readline

n = int(read())
cost = []
dp = [[0 for _ in range(3)] for _ in range(n)]
for i in range(n):
    cost.append(list(map(int, read().split())))
dp[0] = cost[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + cost[i][2]

print(min(dp[n-1]))
