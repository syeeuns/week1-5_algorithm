import sys

# 일단 정렬 1 2 4 8 9
# 간격으로 이진탐색 -> 그 간격으로 설치되는 공유기 수
# 공유기 수 더 많으면 -> 간격 넓힌다
# 공유기 수 더 적으면 -> 간격 좁힌다
# 무조건 맨 첫번째에는 공유기를 설치한다
n, c = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr = sorted(arr)
min_diff = 1
max_diff = arr[-1] - arr[0]
start = min_diff
end = max_diff
answer = 0

while start <= end:
    cnt = 1
    gap = (start + end) // 2
    front = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - front >= gap:
            cnt += 1
            front = arr[i]

    if cnt >= c: # 조건을 만족하는 거니까 여기에 등호
        answer = gap
        start = gap + 1
    else:
        end = gap - 1

print(answer)







# 이진탐색 안 쓴 풀이
# result = []
# for one in combinations(arr, c):
#     temp = []
#     minimum = 1000000001
#     one = sorted(one)
#     for i in range(0, len(one)-1):
#         temp.append(one[i+1]-one[i])
#     result.append(min(temp))
#
# print(max(result))

