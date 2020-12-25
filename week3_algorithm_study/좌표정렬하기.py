import sys
read = sys.stdin.readline

n = int(read())
dots = []
for i in range(n):
    dots.append(list(map(int, read().split())))

dots.sort(key = lambda x: (x[1], x[0]))
for i in dots:
    print(i[0], i[1])