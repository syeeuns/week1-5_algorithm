# 피보나치
# 하나 작은거엔 세로 한줄이 추가될 수 있고, 두개 작은거엔 가로 두줄이 추가될 수 있으므로
import sys
read = sys.stdin.readline

n = int(read())
fibo = [0] * 1001
fibo[1] = 1
fibo[2] = 2
if n > 2:
    for i in range(3, n+1):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 10007
print(fibo[n])