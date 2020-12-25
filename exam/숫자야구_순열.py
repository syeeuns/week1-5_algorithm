import sys, math
read=sys.stdin.readline

def strike(a, b):
    a,b = str(a), str(b)
    cnt = 0
    for i in range(3):
        if a[i] == b[i]:
            cnt += 1
    return cnt

def ball(a, b):
    return len(set(list(str(a))) & set(list(str(b)))) - strike_cnt

answer = set(i for i in range(123,988) if '0' not in str(i) and len(set(list(str(i))))==3)

for _ in range(int(read())):
    num,s,b = map(int,read().split())
    for i in list(answer):
        strike_cnt = strike(i,num)
        if strike_cnt != s or ball(i,num) != b:
            answer -= set([i])

print(len(answer))