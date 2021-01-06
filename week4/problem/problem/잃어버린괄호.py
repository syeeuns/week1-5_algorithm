import sys
read = sys.stdin.readline

# 내 풀이
# s = read().rstrip()
# # 마이너스 나오면 다음 마이너스까지 괄호
# temp = ''
# answer = 0
# flag = 1
# for i in range(len(s)):
#     if 48 <= ord(s[i]) <= 57:
#         temp += s[i]
#     elif s[i] == '-':
#         if flag == 1:
#             answer += int(temp)
#             flag = -1
#         elif flag == -1:
#             answer -= int(temp)
#         temp = ''
#     elif s[i] == '+':
#         if flag == 1:
#             answer += int(temp)
#         elif flag == -1:
#             answer -= int(temp)
#         temp = ''
#
# if flag == 1:
#     answer += int(temp)
# elif flag == -1:
#     answer -= int(temp)
# print(answer)

# 남의 풀이 참고
# 입력받을때 - 기준 나눠서 받고, 걔네는 다 빼기 할거임
# 나눈 애들을 또 + 기준으로 나누고 걔네는 다 더할거임
s = read().rstrip().split('-')
result = []
for one in s:
    temp = one.split('+')
    tt = 0
    for digit in temp:
        tt += int(digit)
    result.append(tt)

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]
print(answer)