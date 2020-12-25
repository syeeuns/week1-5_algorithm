import sys
read = sys.stdin.readline

n = int(read())

# 전체 후보군을 만들고, 하나씩 입력 받을 때마다 후보를 줄여나간다.
# 최종 후보의 개수를 출력한다.
candidate = list(set(i for i in range(123, 988) if '0' not in str(i) and (str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2])))
answer = []

for _ in range(n):
    num, s, b = map(int, read().split())
    s_num = str(num)
    for one in candidate:
        s_one = str(one)
        ball, strike = 0, 0
        for i in range(3):
            if s_num[i] == s_one[i]: strike += 1
        for i in range(3):
            if s_num[i] in s_one: ball += 1
        ball -= strike
        if ball == b and strike == s:
            answer.append(one)
    candidate = answer
    answer = []

print(len(candidate))