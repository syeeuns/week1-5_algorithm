import sys
read = sys.stdin.readline

arr = list(read().rstrip())
stick, answer = 0, 0

while arr:
    temp = arr.pop()
    if temp == ')':
        if arr[-1] == '(': # 레이저
            answer += stick
            arr.pop()
        else:
            stick += 1
    else:
        answer += 1
        stick -= 1


print(answer)