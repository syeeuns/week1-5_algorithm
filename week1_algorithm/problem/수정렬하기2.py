import sys

n = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()
for one in numbers:
    print(one)



