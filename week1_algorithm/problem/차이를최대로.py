from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

permutation = list(permutations(arr, n))
max = 0
for one in permutation:
    temp = 0
    for i in range(n-1):
        temp += abs(one[i]-one[i+1])
    if max < temp:
        max = temp

print(max)