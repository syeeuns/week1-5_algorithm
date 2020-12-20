import sys
read = sys.stdin.readline

n = int(read())
graph = []

for i in range(n):
    graph.append(list(map(int, read().split())))

white_cnt = 0 # 0인 칸
blue_cnt = 0 # 1인 칸
def check(row, col, n):
    global white_cnt, blue_cnt
    cnt = 0
    for i in range(row, row + n):
        for j in range(col, col + n):
            if graph[i][j] == 1:
                cnt += 1
    if cnt == n*n:
        blue_cnt += 1
    elif cnt == 0:
        white_cnt += 1
    else:
        check(row, col, n//2)
        check(row, col+n//2, n//2)
        check(row+n//2, col, n//2)
        check(row+n//2, col+n//2, n//2)


check(0, 0, n)
print(white_cnt)
print(blue_cnt)