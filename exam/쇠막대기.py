import sys
read = sys.stdin.readline

arr = list(read().rstrip())
stack = []
answer = 0
for i in range(len(arr) - 1, -1, -1):
    if not arr:
        break
    if len(arr) >= 2 and arr[-1] == ')' and arr[-2] == '(': # 레이저
        answer += len(stack)
        arr.pop()
        arr.pop()
        if not arr:
            break
    else:
        if arr[-1] == ')':
            answer += 1
            stack.append(arr.pop())
        elif arr[-1] == '(':
            arr.pop()
            stack.pop()

print(answer)


