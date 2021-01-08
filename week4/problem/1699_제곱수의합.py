# 자신보다 작은 가장 큰 제곱수까지 구한다
# i - j**2 는 j**2 만큼 더해주면 i 된다
# dp[j**2] : 제곱수는 dp 값이 1이므로 1 더해주는거임

import sys, math
read = sys.stdin.readline

def solve():
    n = int(read())
    dp = [0] * (n+1)

    for i in range(1, n+1):
        dp[i] = i # 최악의 경우
        for j in range(1, i):
            if j**2 > i: break
            dp[i] = min(dp[i], dp[i - j**2] + 1)  # 기존값과 새로운 값 중 더 작은 걸로 갱신

    print(dp[n])

solve()