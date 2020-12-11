n = int(input())

if n < 100:
    print(n)
else:
    count = 99
    for i in range(100, n+1):
        mod = str(i)
        arr = []
        for one in mod:
            a = int(one)
            arr.append(a)
        if 2*arr[1] == arr[2] + arr[0]:
            count += 1
    print(count)
