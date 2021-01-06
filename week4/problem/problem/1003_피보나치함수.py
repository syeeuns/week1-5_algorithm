import sys
read = sys.stdin.readline

fibo = [[0,0] for _ in range(41)]
fibo[0] = [1,0]
fibo[1] = [0,1]
t = int(read())
for _ in range(t):
    n = int(read())
    for i in range(2, n+1):
        fibo[i][0] = fibo[i-1][0]+fibo[i-2][0]
        fibo[i][1] = fibo[i-1][1]+fibo[i-2][1]
    print(fibo[n][0], fibo[n][1])



