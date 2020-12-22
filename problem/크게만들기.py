import sys
read = sys.stdin.readline

n, k = map(int, read().rstrip().split())
num = list(map(int, read().rstrip())) # 입력된 문자열의 순서를 바꿀 수 없고, 오직 지우기만 가능하다
cnt = 0
stack = [num[0]]
i = 0
# deque
# 앞에서부터 스택에 넣으면서 이미 있는거랑 비교하면서 새거가 더 크면 있는거 더 커질때까지 빼고 넣어줌
for i in range(1, len(num)):
    if num[i] > stack[-1]:
        while stack and stack[-1] < num[i] and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(num[i])
    else:
        stack.append(num[i])
    if cnt == k:
        index = i
        break

if n == k:
    print(0)
elif cnt == k:
    for one in stack:
        print(one, end='')
    for i in range(index+1, len(num)):
        print(num[i], end='')
else:
    for i in range(n-k):
        print(stack[i], end='')





# 시간초과 (for문, list)
# for i in range(n-1):
#     if num[i] <= num[i+1] and cnt < k:
#         del num[i]
#         cnt += 1
#     if cnt == k:
#         break
#
# for i in num:
#     print(i, end='')