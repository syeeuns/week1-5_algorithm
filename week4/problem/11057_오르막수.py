# i번째 자리의 수 <= (i+1)번째 자리의 수
# dp[i][j] : i는 몇번째 자리수인지, j는 그걸로 끝나는 i자리수
# 예를 들어 dp[2][8] 이면, 8로 끝나는 두자리 오르막수의 갯수
import sys
read = sys.stdin.readline

n = int(read())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[1] = [1] * 10
for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = (sum(dp[i-1][:j+1])) % 10007
print(sum(dp[n]) % 10007)