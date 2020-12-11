T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    for one in S:
        print(one * R, end='')
    print()
