n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
arr.sort()
'\n'.join(arr)
for one in arr:
    print(one)