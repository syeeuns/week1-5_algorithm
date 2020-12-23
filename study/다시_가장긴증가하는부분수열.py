import sys, bisect
read = sys.stdin.readline

n = int(read().rstrip())
nums = list(map(int, read().rstrip().split()))

#dp
# 이중포문 써야함!!!! dp 배열은 해당 원소까지의 최장 길이를 저장함
# dp = [1 for _ in range(n)]
# for i in range(1, n):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))
#

# binary search
result = [nums[0]]
for i in range(1, n):
    if nums[i] == result[-1]: continue
    elif nums[i] > result[-1]:
        result.append(nums[i])
    else:
        new = bisect.bisect_right(result, nums[i])
        if result[new-1] == nums[i]:
            continue
        else: result[new] = nums[i]

print(len(result))
