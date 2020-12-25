n = int(input())
candidate = []
temp = []

# 100~999 숫자를 담자
for i in range(100, 1000):
    # 자리수 숫자 겹치거나 or 0 포함하거
    if str(i)[0] == str(i)[1] or str(i)[0] == str(i)[2] or str(i)[1] == str(i)[2] or str(i)[0] == '0' or str(i)[1] == '0' or str(i)[2] == '0':
        continue
    else:
        candidate.append(i)

# ball, strike 체크하면서 후보군 찾자
for i in range(n):
    num, strike, ball = map(int, input().split())
    for j in candidate:
        s = 0
        b = 0
        s_num = str(num)
        s_j = str(j)
        if s_num[0] == s_j[0]: s += 1
        if s_num[1] == s_j[1]: s += 1
        if s_num[2] == s_j[2]: s += 1
        if s_j[0] == s_num[1]: b += 1
        if s_j[0] == s_num[2]: b += 1
        if s_j[1] == s_num[0]: b += 1
        if s_j[1] == s_num[2]: b += 1
        if s_j[2] == s_num[0]: b += 1
        if s_j[2] == s_num[1]: b += 1
        if s == strike and b == ball:
            temp.append(j)
    candidate = temp
    temp = []

print(len(candidate))

