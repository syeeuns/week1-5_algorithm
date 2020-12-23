import sys
read = sys.stdin.readline

n = int(read().rstrip())
for i in range(n):
    vps = list(read().rstrip())

    if vps[0] == ')' or vps[-1] == '(':
        print('NO')
        continue

    else:
        stack = []
        while len(vps):
            if vps[-1] == ')':
                stack.append(vps.pop())
            elif vps[-1] == '(':
                if stack:
                    vps.pop()
                    stack.pop()
                else:
                    print('NO')
                    break
        else:
            if stack: print('NO')
            else: print('YES')