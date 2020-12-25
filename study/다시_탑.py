import sys
read = sys.stdin.readline

n = int(read())
tower = list(map(int, read().split()))
stack = [[0, tower[0]]] # 스택에 타워 인덱스, 높이 같이 리스트로 담자
answer = ['0']

for i in range(1, n):
    # 스택에 자신보다 작은게 있으면 pop, 큰 거 만날 때까지 반복
    # 무조건인덱스랑 높이 저장,  스택 비면 0 출력
    while stack:
        if stack[-1][1] < tower[i]:
            stack.pop()
        else:
            answer.append(str(stack[-1][0]+1))
            break

    if not stack:
        answer.append('0')
    stack.append([i, tower[i]])

print(' '.join(answer))