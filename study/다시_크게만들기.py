import sys
read = sys.stdin.readline

n, k = map(int, read().split())
number = read().rstrip()

if n==k:
    print(0)
    exit()

cnt = 0
stack = [number[0]]
for i in range(1, n):
    while stack and stack[-1] < number[i] and cnt < k:
        stack.pop()
        cnt += 1
    stack.append(number[i])

print(''.join(stack[:n-k]))
