import sys, heapq
read = sys.stdin.readline

n = int(read().rstrip())
heap = []
for i in range(n):
    heapq.heappush(heap, int(read()))

answer = 0
while len(heap) > 1:
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    answer += temp
    heapq.heappush(heap, temp)


print(answer)

