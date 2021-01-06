# 마지막 계단은 반드시 밟아야한다
# 첫번째 계단은 안밟아도된다
# dp[i][1] : 연속 1개의 계단을 밟고 i번째에 와있다 (직전꺼 밟지 않았다)
# dp[i][2] : 연속 2개의 계단을 밟고 i번째에 와있다 (직전꺼 밟았다)
import sys
read = sys.stdin.readline

n = int(read())
# 밟는 계단의 최댓값 계산
dp = [[0, 0, 0] for _ in range(n+1)]
stair = [0]
for _ in range(n):
    stair.append(int(read()))
dp[1] = [0, stair[1], 0]
for i in range(2, n+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stair[i]
    dp[i][2] = dp[i-1][1] + stair[i]

print(max(dp[n][1], dp[n][2]))



