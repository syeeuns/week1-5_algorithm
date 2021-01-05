import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
# # prefix sum
# sum_arr = [0] * n
# for i in range(1, n):
#     sum_arr[i] = sum_arr[i-1] + arr[i]
#
# # 인덱스 a~b 구간합은 sum_arr[b] - sum_arr[a-1]
# result = max(arr)
# for a in range(1, n):
#     for b in range(a+1, n):
#         result = max((sum_arr[b] - sum_arr[a-1]), result)
#
# print(result)

# dp
# dp[i] : arr의 i번째 항을 마지막값으로 하는 최댓값
# dp[i-1] < 0 이면 안더하고 그냥 지금 값만으로 새 합 만드는 것이 나음
dp = [0] * n
dp[0] = arr[0]
if n == 1:
    print(dp[0])
    exit()
for i in range(1, n):
    dp[i] = max(0, dp[i-1]) + arr[i]
print(max(dp))

