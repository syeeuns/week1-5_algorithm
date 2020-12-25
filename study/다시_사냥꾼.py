import sys, bisect
read = sys.stdin.readline

m, n, l = map(int, read().split())
hunter = sorted(list(map(int, read().split())))
animal = []
for i in range(n):
    animal.append(list(map(int, read().split())))

# y좌표 기준 오름차순 정렬
animal.sort(key=lambda x: x[1])
cnt = 0
for i in range(n):
    distance = l - animal[i][1]
    if distance < 0: # y좌표만 봐도 사정거리를 넘어간다면 그 뒤 동물은 쳐다도 안본다.
        break

    # 라이브러리 이용
    else:
        possible_start = animal[i][0] - distance
        possible_end = animal[i][0] + distance
        binary_start = bisect.bisect_right(hunter, possible_start)
        binary_end = bisect.bisect_right(hunter, possible_end)
        # 동물 범위가 사대 범위 안에 있는데 정확히 사대에 걸리지 않는 경우 조건 추가해주기
        if bisect.bisect_left(hunter, possible_start) == m: # 범위가 더 크거나
            continue
        elif binary_end == 0: # 범위가 더 작으면
            continue
        elif binary_start == binary_end and possible_start != hunter[binary_start - 1]:
            continue
        else: cnt += 1


    # 이진탐색 직접 구현
    # else: # animal[i][0] +- distance 범위 안에 해당하는 사대가 하나라도 있는지
    #     start = 0
    #     end = m - 1
    #     possible_start = animal[i][0] - distance
    #     possible_end = animal[i][0] + distance
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if possible_start <= hunter[mid] <= possible_end:
    #             cnt += 1
    #             break
    #         elif hunter[mid] < possible_start:
    #             start = mid + 1
    #         elif hunter[mid] > possible_end:
    #             end = mid - 1

print(cnt)


