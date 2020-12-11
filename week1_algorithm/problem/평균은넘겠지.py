C = int(input())

for i in range(C):
    arr = list(map(int, input().split()))
    students = arr[0]
    arr.pop(0)
    average = sum(arr) / len(arr)
    cnt = 0
    for one in arr:
        if one > average:
            cnt += 1
    print(f'{format(round(cnt/len(arr)*100, 3), ".3f")}%')


