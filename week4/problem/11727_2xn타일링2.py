# 타일링 문제는 점화식을 찾기 위해 왼쪽 상단 가장 작은 정사각형을 덮는 것을 생각해보면 된다.
# 1. 1*2 타일이 덮는 경우 -> f(n-1)
# 2. 2*1 타일이 덮는 경우 -> f(n-1)
# 3. 2*2 타일이 덮는 경우 -> f(n-2)
import sys
read = sys.stdin.readline

n = int(read())
dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append((dp[i-1] + 2*dp[i-2]) % 10007)
print(dp[n])