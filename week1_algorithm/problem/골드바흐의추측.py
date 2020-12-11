prime_number = [2, 3, 5, 7,11, 13,]

# 소수 판별
def is_prime(n):
    if n in prime_number:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            for i in range(3, n, 2):
                if n % i == 0:
                    return False
            if n not in prime_number:
                prime_number.append(n)
            return True

# 2씩 덜어주고 판별
def is_prime_2(a, b):
    while True:
        a -= 2
        b += 2
        if is_prime(a) and is_prime(b):
            print(f'{a} {b}')
            return



T = int(input())
for i in range(T):
    number = int(input())
    half = number//2

    if number == 4:
        print(f'{half} {half}')
        continue

    elif is_prime(half):
        print(f'{half} {half}')
        continue

    elif (half) % 2 == 0:
        a = half - 1
        b = half + 1
        if is_prime(a) and is_prime(b):
            print(f'{a} {b}')
        else:
            is_prime_2(a, b)

    else:
        is_prime_2(half, half)
