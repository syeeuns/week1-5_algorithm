import sys
read = sys.stdin.readline

# 양수, 음수 있는 배열에서 2개 숫자 뽑아 더해서 0에 가장 가까워지는 경우 찾기
# 목표값은 0
n = int(read())
solution = sorted(list(map(int, read().split())))
# 투 포인터
# 양쪽 끝값 더해서 값, 인덱스 저장
# 더한 값이 음수면 start += 1
# 더한 값이 양수면 end -= 1
# 새로운 값과 저장된 값 절대값 비교해서 더 작은 애로 인덱스까지 갱신
# start == end 될 때까지 반복

start = 0
end = n-1
before = 10000000001
best = [before, 0, 0]

while start != end:
    mix = solution[start] + solution[end]
    if abs(mix) < abs(best[0]):
        best[0] = mix
        best[1] = solution[start]
        best[2] = solution[end]

    if mix == 0:
        break
    elif mix < 0:
        start += 1
    else:
        end -= 1

print(best[1], best[2])