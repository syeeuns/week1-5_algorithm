import sys
read = sys.stdin.readline

a, b, c = map(int, read().rstrip().split())

def calculate(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 1:
        temp = calculate(a, b // 2, c)
        return ((temp **2)  * a) % c
    else:
        temp = calculate(a, b // 2, c)
        return (temp ** 2) % c

if a == c or c == 1:
    print(0)
else:
    print(calculate(a, b, c))