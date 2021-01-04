# 아이디어
# 1. 비어있는 곳이 있으면 꽂는다
# 비어있는 곳이 없으면?
# 2. 이미 자신이 꽂혀있다면 냅둔다
# 3. 아니라면, 다시 안쓰이거나 가장 나중에 다시 쓰이는 애를 뽑는다

# 구현
# 멀티탭을 n만큼 배열 선언
# 사용 순서를 k만큼 배열 선언
# 멀티탭 배열에 0이 있으면 아직 안꽂힌거니까 k만큼 for문 돌면서 확인하고 꽂는다
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
use = list(map(int, read().split()))
multitap = [0] * n
cnt = 0

for i in range(k):
    if use[i] in multitap: # 이미 꽂혀있으면 냅둔다
        continue
    elif 0 in multitap: # 비어있으면 꽂는다
        multitap[multitap.index(0)] = use[i]
    else: # 비어있는 곳이 없으며, 이미 꽂혀있지도 않은 경우엔 2가지 따진다. 다시 쓰이는지 안쓰이는지
        max_index = i
        for j in range(n):
            if multitap[j] not in use[i:]: # 다시 안쓴다면 뽑아버린다
                swap = j
                break
            else: # 뒤에 다시 쓰인다면 가장 큰 인덱스로 갱신
                now = use[i:].index(multitap[j]) + i
                if max_index < now:
                    max_index = now
                swap = multitap.index(use[max_index])
        multitap[swap] = use[i]
        cnt += 1
print(cnt)

# '이미 꽂혀있으면 냅둔다' 와 '비어있으면 꽂는다' 의 순서가 바뀌면 안됨
# 무조건 '이미 꽂혀있으면 냅둔다'를 먼저 처리해줘야함
# 만약 2가 꽂혀있는데 빈 콘센트가 있는 상태에서 2가 또 나왔다면?
# 비어있으면 꽂는다를 먼저 처리하는 경우, 2를 새 콘센트에 또 꽂게 됨
