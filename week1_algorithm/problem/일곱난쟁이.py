from itertools import combinations

heights = []
for _ in range(9):
    n = int(input())
    heights.append(n)

comb = list(combinations(heights, 7))
result = []
for one in comb:
    if sum(one) == 100:
        result = list(one)
        break

result.sort()
for i in result:
    print(i)