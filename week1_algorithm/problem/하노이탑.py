# 하노이탑 원반 개수 n개면 이동 횟수 2^n -1
def move(n, start, stop):
    if n == 1:
        print(f'{start} {stop}')
        return
    else:
        move(n-1, start, 6-start-stop)
        print(f'{start} {stop}')
        move(n - 1, 6 - start - stop, stop)


def move_big(n, start, stop):
    if n == 1:
        return
    else:
        move_big(n-1, start, 6-start-stop)
        move_big(n - 1, 6 - start - stop, stop)


n = int(input())
if n > 20:
    print(2**n-1)
else:
    print(2**n-1)
    move(n, 1, 3)

