a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)

arr = [0] * 10

for one in num:
    one = int(one)
    arr[one] += 1

for one in arr:
    print(one)