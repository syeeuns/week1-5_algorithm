import sys
read = sys.stdin.readline

i = 0
while True:
    i += 1
    l, p, v = map(int, read().split())
    if l == 0 and p == 0 and v == 0: break
    answer = (v // p) * l
    if (v % p) <= l: answer += v % p
    elif (v % p) > l: answer += l
    print(f'Case {i}: {answer}')
