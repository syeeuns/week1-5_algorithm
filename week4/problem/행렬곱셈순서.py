
import sys
read = sys.stdin.readline

n = int(read())
matrix = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, read().split())))

for i in range(n-1): # 두개씩 곱하는 연산횟수를 dp테이블에 채운다
    dp[i][i+1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]


for k in range(2, n): # dp테이블 대각선 사이클 돈다 (같은 대각선 사이클에 있다 => 행,열 차가 같다)
    for i in range(n-k): # 행 시작점
        j = i + k
        dp[i][j] = 2**32
        for x in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][x] + dp[x+1][j] + matrix[i][0]*matrix[x][1]*matrix[j][1])

print(dp[0][n-1])

# dp[i][j] 를 i번째에서 j번째 행렬 곱하는 최솟값으로
#
# dp[i][k]   dp[k+1][j] 로 쪼갠다
# A BCDE
# AB CDE
# ABC DE
# ABCD E
# 그러면 i의 row * k의 col * j의 col
# 하면 세 개 곱할때지