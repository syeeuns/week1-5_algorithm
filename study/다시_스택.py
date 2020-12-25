import sys
read = sys.stdin.readline

n = int(read())
stack = []
for i in range(n):
    arr = read().split()
    if arr[0] == 'push':
        stack.append(int(arr[1]))
    elif arr[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    elif arr[0] == 'size':
        print(len(stack))
    elif arr[0] == 'empty':
        if stack: print(0)
        else: print(1)
    elif arr[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)
