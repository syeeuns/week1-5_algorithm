import sys
read = sys.stdin.readline

while True:
    temp = list(map(int, read().rstrip().split()))
    if temp == ['0']:
        break
    a, arr = temp[0], temp[1:]

