import sys, heapq
read = sys.stdin.readline

n = int(read())

heap = []
for i in range(n):
    num = int(read())
    if num == 0:
        if len(heap) == 0:
            print(0)
            continue
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)
