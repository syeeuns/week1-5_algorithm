# dp[i][j] : i자리수이며 j로 끝나는 계단수의 개수
# i : 몇 자리수
# j : 계단수가 j로 끝난다
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# 끝에서부터 한자리씩 고정시켜가며 찾으면 점화식 도출 가능ㅇ
# 이차원 테이블이 어려우면, 이차원 배열이라고 생각하지 말고
# 그냥 따라서 변화하는 정보가 2가지 있다고 생각하자
# 0~9까지 숫자 다 쓸거라서 양쪽에 -1, 10 위치에 열 추가해줌 (총 12개)
import sys
read = sys.stdin.readline

n = int(read())
dp = [[0 for _ in range(12)] for _ in range(n+1)]
dp[1] = [0,0,1,1,1,1,1,1,1,1,1,0]
for i in range(2, n+1):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)
