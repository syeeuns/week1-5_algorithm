import sys
read = sys.stdin.readline

n = int(read())
predict = []
real = [i for i in range(1, n+1)]
for _ in range(n):
    predict.append(int(read()))
predict.sort()
answer = 0
for i in range(n):
    answer += abs(predict[i] - real[i])

print(answer)
