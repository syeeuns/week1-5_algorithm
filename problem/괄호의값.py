import sys
read = sys.stdin.readline

a = list(read().rstrip())
stack = []
answer = 0
temp = 1

if a[0] == ')' or a[0] == ']': # 잘못된 문자열
    answer = 0
else: # 스택이 비어있는지 여부가 상관없는 문제 (왜냐면 괄호 끊어져도 또 새거 나올 수 있으니까) 
    for i in range(len(a)-1, -1, -1):
        if (a[i] == '(' or a[i] == '[') and not stack: # 잘못된 문자열
            answer = 0
            break
        elif a[i] == ')':
            stack.append(a[i])
            temp *= 2
        elif a[i] == ']':
            stack.append(a[i])
            temp *= 3
        elif a[i] == '(':
            if stack[-1] == ')':
                if a[i+1] == ')': # 이전 괄호랑 닫혀질때 더해주기
                    answer += temp
                stack.pop()
                temp //= 2
        elif a[i] == '[':
            if stack[-1] == ']':
                if a[i+1] == ']': # 이전 괄호랑 닫혀질때 더해주기
                    answer += temp
                stack.pop()
                temp //= 3

    if stack:
        answer = 0

print(answer)


