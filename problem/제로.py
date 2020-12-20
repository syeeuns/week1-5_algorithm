import sys
n = int(sys.stdin.readline().rstrip())

stack = []
for i in range(n):
    price = int(sys.stdin.readline().rstrip())
    if price == 0:
        stack.pop()
    else:
        stack.append(price)

print(sum(stack))