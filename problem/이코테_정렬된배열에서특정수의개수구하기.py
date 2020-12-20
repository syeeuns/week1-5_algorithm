import sys
from bisect import bisect_left, bisect_right

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 일단 x를 이분탐색으로 찾는다.
# end - start

# def binary_search(arr, key, start, end):
#     center = (start+end) // 2
#
#     if arr[center] == key:
#         return center
#     elif arr[center] > key:
#         return binary_search(arr, key, start, center-1)
#     else:
#         return binary_search(arr, key, center+1, end)

# 라이브러리 이용한 개꿀 풀이
answer = bisect_right(arr, x) - bisect_left(arr, x)
if answer == 0:
    print(-1)
else:
    print(answer)