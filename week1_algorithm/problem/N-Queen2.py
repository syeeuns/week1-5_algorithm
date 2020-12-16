# 열끼리 뺀거, 행끼리 뺀거의 절댓값이 같으면 같은 대각선 위에 있다
import sys
cnt = 0

def n_queens(i, col):
    n = len(col) -1
    if(promising(i, col)):
        if(i==n):
            # print(col[1:])
            global cnt
            cnt += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)


def promising(i, col):
    k =1
    flag = True
    while(k<i and flag):
        if(col[i]==col[k] or abs(col[i]-col[k])==abs(i-k)):
            flag = False
        k += 1
    return flag



n = int(sys.stdin.readline().rstrip())
col = [0] * (n+1)
n_queens(0, col)
print(cnt)