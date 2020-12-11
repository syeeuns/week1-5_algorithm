n = int(input())

for j in reversed(range(n)):
    print(' ' * j, end='')
    print('*' * (n-j))



