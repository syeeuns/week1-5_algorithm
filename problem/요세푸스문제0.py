import sys
read = sys.stdin.readline

n, k = map(int, read().split())
arr = [i for i in range(1, n+1)]
result = []

index = 0
while True:
    if len(arr) == 1:
        result.append(arr[0])
        break
    elif (index + k - 1) < len(arr):
        result.append(arr[index + k-1])
        del arr[index + k - 1]
        index += k - 1
    else:
        index = (index + k - 1) % len(arr)
        result.append(arr[index])
        del arr[index]

print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(f'{result[-1]}>')
