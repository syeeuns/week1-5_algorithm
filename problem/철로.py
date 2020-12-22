import sys
read = sys.stdin.readline

n = int(read())
people = []
for i in range(n):
    people.append(list(map(int, read().rstrip().split())))
d = int(read())

