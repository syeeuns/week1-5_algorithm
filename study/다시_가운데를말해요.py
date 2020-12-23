import sys
from heapq import heappop, heappush
read = sys.stdin.readline

n = int(read().rstrip())
max_heap = []
min_heap = []

for i in range(n):
    num = int(read())
    if i % 2 == 0:
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        temp_max = -heappop(max_heap)
        temp_min = heappop(min_heap)
        heappush(max_heap, -temp_min)
        heappush(min_heap, temp_max)

    print(-max_heap[0])