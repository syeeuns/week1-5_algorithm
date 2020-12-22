import sys, bisect
read = sys.stdin.readline

n = int(read().rstrip())
arr = list(map(int, read().rstrip().split()))
# 1. dp
# dp[i] = i번째 원소를 마지막으로 하는 가장 긴 증가하는 부분 수열의 길이
dp = [1 for _ in range(1002)]
for i in range(0, len(arr)):
    last_val = arr[i]
    for j in range(i+1):
        compare_val = arr[j]
        if compare_val < last_val:
            # j까지의 dp값에 현재 1만큼 더한거랑, 갱신한 dp[i]값 비교해서 더 큰 값으로 계속 갱신
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 2. binary search
# result에 담으면서 새로 들어올 값을 이진탐색으로 어느 위치에 들어갈지 확인
# 이진탐색한 오른쪽 위치꺼 갱신해줌 bisect_right
# result = [arr[0]]
# for i in range(1, len(arr)):
#     if result[-1] < arr[i]:
#         result.append(arr[i])
#     elif result[-1] == arr[i]:
#         continue
#     else:
#         new = bisect.bisect_right(result, arr[i])
#         if result[new-1] == arr[i]:
#             continue
#         else: result[new] = arr[i]
#
# print(len(result))