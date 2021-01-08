# 배낭이랑 완전 똑같음
# dp[i][j]
# i: 지금 잔
# j: 지금 잔까지 연속된 잔 수 (1,2)
# dp테이블 그려보면 점화식 도출 가능
import sys
read = sys.stdin.readline

n = int(read())
wine = [0, ]
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for _ in range(n):
    wine.append(int(read()))
dp[1][1], dp[1][2] = wine[1], wine[1]

for i in range(2, n+1):
    dp[i][1] = max(dp[i-2]) + wine[i]
    dp[i][2] = max(dp[i-1][2], dp[i-1][1] + wine[i])

print(max(dp[n]))