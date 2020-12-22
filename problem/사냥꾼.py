import sys, bisect
read = sys.stdin.readline

hunter_num, animal_num, limit = map(int, read().split())
hunter = sorted(list(map(int, read().rstrip().split())))

animal = []
for i in range(animal_num):
    animal.append(list(map(int, read().rstrip().split())))

# 이진탐색 구현
cnt = 0
for one in animal:
    start = 0
    end = hunter_num - 1
    while start <= end:
        mid = (start + end) // 2
        if abs(hunter[mid] - one[0]) + one[1] <= limit:
            cnt += 1
            break
        else:
            if hunter[mid] > one[0]:
                end = mid - 1
            else:
                start = mid + 1

print(cnt)



# 내 풀이
# cnt = 0
# for one in animal:
#     index = bisect.bisect_right(hunter, one[0])
    # 오른쪽 밖으로 나가버리는 경우
#     if index == hunter_num:
#         distance = one[0] - hunter[-1] + one[1]
#     # 0 나오는 경우
#     elif index == 0:
#         distance = hunter[0] - one[0] + one[1]
#     else:
#         candidate = min(hunter[index] - one[0], one[0] - hunter[index - 1])
#         distance = candidate + one[1]
#
#     if distance <= limit:
#         cnt += 1
#
# print(cnt)

# 남의 풀이 참고한 풀이
# cnt = 0
# for one in animal:
#     index = bisect.bisect_right(hunter, one[0])
#     if (index < hunter_num and hunter[index] - one[0] + one[1] <= limit) or (
#             index > 0 and one[0] - hunter[index - 1] + one[1] <= limit):
#         cnt += 1
#
# print(cnt)


############### 남의 풀이
# import sys
# from bisect import bisect_right
#
# m, n, l = list(map(int, sys.stdin.readline().strip().split()))
# shooting_spots = list(map(int, sys.stdin.readline().strip().split()))
#
# shooting_spots.sort()
#
# answer = 0
# for _ in range(n):
#     x, y = list(map(int, sys.stdin.readline().strip().split()))
#     idx = bisect_right(shooting_spots, x)
#     if (idx < m and shooting_spots[idx] - x + y <= l) or (0 < idx and x - shooting_spots[idx - 1] + y <= l):
#             answer += 1
# print(answer)









