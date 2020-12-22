import sys
read = sys.stdin.readline

a, b, c = map(int, read().split())

def check(a, b, c):
    if b == 1:
        return a
    elif b % 2 == 0:
        return (check(a, b//2, c) ** 2) % c
    elif b % 2 == 1:
        return (a*(check(a, (b-1)//2, c) ** 2)) % c

if a == c:
    print(0)

else:
    # 재귀
    # 1. b=1까지 타고 내려가서 올라오는 방법
    print(check(a, b, c)%c)


