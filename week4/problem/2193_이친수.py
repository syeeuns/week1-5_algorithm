# 끝자리 0,1인 경우 나눠서 쓰다보면 피보나치인거 알 수 있음
# 점화식으로 도출해보자면 dp[i][j] : i는 길이, j는 끝나는 수
# dp[i][0] = dp[i-1][0] + dp[i-1][1]
# dp[i][1] = dp[i-1][0]
# 0으로 끝나는 거는 전에꺼 다 들어감
# 1로 끝나는 거는 전에 0으로 끝나는 것만
import sys
read = sys.stdin.readline

n = int(read())
# 그냥 피보  76ms
# fibo = [0,1,1]
# for i in range(3, n+1):
#     fibo.append(fibo[i-1]+fibo[i-2])
# print(fibo[n])

# 점화식   64ms
dp = [[0, 0] for _ in range(n+1)]
dp[1] = [0, 1]
for i in range(2, n+1):
    dp[i] = [dp[i-1][0] + dp[i-1][1], dp[i-1][0]]
print(sum(dp[n]))