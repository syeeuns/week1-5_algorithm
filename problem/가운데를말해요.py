import sys, heapq
read = sys.stdin.readline

n = int(read())
max_heap = []
min_heap = []
for i in range(n):
    num = int(read())
    # max_heap 중앙값 min_heap
    # max_heap root < min_heap root
    # 하나씩 번갈아 넣어주면서, max_heap 에 더 큰거 들어오면 바꿔주기
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if i == 0:
        print(-max_heap[0])
        continue
    # 하나씩 번갈아 넣어주면서, max_heap 에 더 큰거 들어오면 바꿔주기
    elif -max_heap[0] > min_heap[0]:
        max_temp = -heapq.heappop(max_heap)
        min_temp = heapq.heappop(min_heap)
        heapq.heappush(min_heap, max_temp)
        heapq.heappush(max_heap, -min_temp)
    print(-max_heap[0])