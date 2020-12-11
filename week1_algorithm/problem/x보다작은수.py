import sys

N, X = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    if i < X:
        print(i, end=' ')