# 빈 콘센트가 있으면 멀티탭에 꽂는다
# 다시 사용안하거나 더 나중에 다시 사용하는 애를 뽑는다
import sys
from collections import defaultdict
read = sys.stdin.readline

n, k = map(int, read().split())
use = list(map(int, read().split()))
multitap = [0] * n
cnt = 0
for i in range(k):
    if use[i] in multitap: # 이미 꽂혀있으면
        continue
    elif 0 in multitap: # 빈 멀티탭 있으면 꽂는다
        multitap[multitap.index(0)] = use[i]
    else: # 빈 멀티탭 없으면
        max_index = i
        swap = 0
        for j in range(n):
            if multitap[j] in use[i:]: # 이후에 사용하는 경우가 있으면 가장 나중에 사용하는 애 뽑자
                temp = use[i:].index(multitap[j]) + i
                if max_index < temp:
                    max_index = temp
                swap = multitap.index(use[max_index])
            else: # 사용하는 경우 없으면 얠 뽑자
                swap = j
                break
        multitap[swap] = use[i]
        cnt += 1
print(cnt)

# 1 2 3 4 1 2
# 2 3 2 3 1 2 7