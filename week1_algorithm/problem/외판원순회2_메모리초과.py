import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for_travel = list(permutations([i for i in range(n)]))

cost = 0
min = 999
for one in for_travel:
    for i in range(len(one)):
        if i == len(one)-1:
            cost += graph[one[i]][one[0]]
        else:
            cost += graph[one[i]][one[i+1]]
    if min > cost:
        min = cost
    cost = 0

print(min)
