import sys, heapq
read = sys.stdin.readline

n = int(read().rstrip())
heap = []
for i in range(n):
    num = int(read())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))