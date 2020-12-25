import sys
read = sys.stdin.readline

n = int(read().rstrip())
stack = []
for i in range(n):
    num = int(read())
    stack.append(num) if num else stack.pop()

print(sum(stack))
