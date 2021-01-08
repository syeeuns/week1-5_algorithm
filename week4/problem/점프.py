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

# i-v 에서 속도 v로 i에 들어오는 경우는
# v+1 속도에서 감속점프하면서 들어온거,
# v 속도에서 유지하면서 들어온거,
# v-1속도에서 늘리면서 들어온거 이렇게 3가지
# 그러면
#
# dp[현재 내위치][이 위치에 들어온 속도]
#
# dp[i][v] = min(dp[i-v][v+1], dp[i-v][v], dp[i-v][v-1]) + 1
#
# 낼수있는 속도는 (목표지 * 2)^(1/2)
#
# 이건 n(n+1)/2 = 목표지 니까
# N^2 = 2목표지    에서 나오는거
# 대충 저거의 올림하거나 +1해서 쓰기
