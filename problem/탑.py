import sys
read = sys.stdin.readline

n = int(read())
tower = list(map(int, read().rstrip().split()))
stack = [(1, tower[0])]
result = ['0']

# 앞에서부터 접근
# 처음은 0이고, stack에 넣는다
# 다음꺼랑 비교하고, 다음꺼가 더 크면 지금꺼는 stack에서 꺼내고, 다음꺼를 stack에 넣음
# 다음꺼랑 비교하고, 다음꺼가 더 작으면 지금꺼는 그냥 두고, 다음꺼는 stack에 넣음

for i in range(1, n):
    while stack:
        if stack[-1][1] < tower[i]:
            stack.pop()
        else:
            result.append(str(stack[-1][0]))
            break
    if not stack:
        result.append('0')
    stack.append((i+1, tower[i]))

print(' '.join(result))



# 시간초과 (이중포문)
# for i in range(n-1, 0, -1):
#     temp = 0
#     for j in range(i-1, -1, -1):
#         if tower[j] >= tower[i]:
#             result.append(str(j+1))
#             temp = 1
#             break
#         else:
#             temp = 0
#
#     if temp == 0: result.append('0')
#
# result.append('0')
# print(' '.join(result[::-1]))