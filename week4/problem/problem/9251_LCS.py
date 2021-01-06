import sys
read = sys.stdin.readline

str1 = read().rstrip()
str2 = read().rstrip()
n, m = len(str1), len(str2)
dp = [[0 for _ in range(1001)] for _ in range(1001)]
# max(dp[i-1][j], dp[i][j-1])
# 같은 거 만나면 max값에 +1
# 문자열은 0번 인덱스부터 n,m까지니까 인덱스 -1 해주기
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
