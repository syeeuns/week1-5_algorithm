n = int(input())
target = n
cnt = 0

def cycle(n, cnt):
    one = n // 10
    two = n % 10
    new = two * 10 + (one + two) % 10

    if n == target and cnt != 0:
        print(cnt)
        return

    cnt += 1
    cycle(new, cnt)



cycle(n, cnt)