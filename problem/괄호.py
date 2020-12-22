import sys
read = sys.stdin.readline

n = int(read())
for i in range(n):
    vps = list(read().rstrip())
    if vps[0] == ')':
        print('NO')
        continue
    else:
        temp = []
        while len(vps) > 0:
            if vps[-1] == ')':
                temp.append(vps.pop())
            elif vps[-1] == '(':
                if temp:
                    temp.pop()
                    vps.pop()
                else:
                    print('NO')
                    break
        if temp:
            print('NO')
        elif len(vps) == 0:
            print('YES')