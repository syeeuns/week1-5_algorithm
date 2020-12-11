T = int(input())

for i in range(T):
    arr = input()
    score = 0
    sum = 0
    for j in range(len(arr)):
        if arr[j] == 'O':
            score += 1
            sum += score
        elif arr[j] == 'X':
            score = 0
    print(sum)
