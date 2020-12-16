# 메모리 초과남
# 방문했던 곳은 안 가는 식으로 다시 구현해보
import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
permutation_seed = [i for i in range(n)]
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def check_route(c):
    cost = 0
    for i in range(n-1):
        if graph[c[i]][c[i+1]] != 0:
            cost += graph[c[i]][c[i+1]]
        else:
            return -1

    if graph[c[-1]][c[0]] != 0:
        cost += graph[c[-1]][c[0]]
    else:
        return -1
    return cost


min = 99999999
for c in permutations(permutation_seed):
    result = check_route(c)
    if check_route(c) != -1:
        if result < min:
            min = result

print(min)






