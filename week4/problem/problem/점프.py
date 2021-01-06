import math
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
max_speed = math.ceil(1.414*(n**0.5))
no_stone = []
dp = [[float('inf') for _ in range(max_speed+1)] for _ in range(n+1)]
dp[1][0] = 0
for _ in range(m):
    no_stone.append(int(read()))

for i in range(2, n+1):
    if i in no_stone:
        continue # 돌없는 줄은 넘어간다 인피니티로 둠
    for v in range(1, max_speed):
        if i - v < 0:
            break
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

result = min(dp[n])
print(min(dp[n]) if result != float('inf') else -1)
