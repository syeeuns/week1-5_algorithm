import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

a = sorted(a)
def binary_search(a, key):
    pl = 0
    pr = len(a) -1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc+1
        else:
            pr = pc-1
        if pl > pr:
            return 0

for one in b:
    print(binary_search(a, one))