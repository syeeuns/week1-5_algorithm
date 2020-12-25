import sys
r = sys.stdin.readline

#특정 시점에 존재하는 막대기 개수 : stick
stick = 0
string = list(r().strip())
answer = 0

while string:

    #하나씩 빼면서 확인
    x = string.pop()

    if x ==')':
        if string[-1] == '(':
            answer += stick
            string.pop()
        else:
            stick += 1
    else:
        answer += 1
        stick -= 1

print(answer)
