import sys
read = sys.stdin.readline

n = int(read())
dp = [1000001] * 1000001

# bottom-up
# dp[1] = 0
# i = 1
# while i < n:
#     dp[i*3] = min(dp[i*3], dp[i] + 1)
#     dp[i * 2] = min(dp[i * 2], dp[i] + 1)
#     dp[i + 1] = min(dp[i + 1], dp[i] + 1)
#     i += 1
# print(dp[n])

#top-down
temp = n
dp[temp] = 0
for temp in range(n, 0, -1):
    if temp % 3 == 0:
        dp[temp//3] = min(dp[temp//3], dp[temp]+1)
    if temp % 2 == 0:
        dp[temp//2] = min(dp[temp//2], dp[temp]+1)
    dp[temp-1] = min(dp[temp-1], dp[temp]+1)

print(dp[1])