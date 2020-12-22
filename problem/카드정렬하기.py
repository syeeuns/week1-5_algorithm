import sys, heapq
read = sys.stdin.readline

n = int(read())
cards = []
temp = []
for i in range(n):
    heapq.heappush(cards, int(read()))

if n == 1:
    answer = 0

else:
    answer = 0
    while len(cards) > 1:
        temp1 = heapq.heappop(cards)
        temp2 = heapq.heappop(cards)
        subsum = temp1 + temp2
        answer += subsum
        heapq.heappush(cards, subsum)

print(answer)