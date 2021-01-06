# 서류 기준 오름차순 정렬한다
# 서류 1위는 무조건 채용한다
# 2위부터 차례로 붙여본다
# 채용하면서 면접점수 마지노선을 계속 더 빡센 기준으로 업데이트해준다
# 왜냐하면 서류 등수는 점점 커지는데 면접점수는 점점 작은 애들을 채용할거니까 작은애로 업뎃해줘야징

import sys
read = sys.stdin.readline

def solve():
    t = int(read())
    for _ in range(t):
        rank = []
        employed = []
        n = int(read())
        for _ in range(n):
            rank.append(list(map(int, read().split())))
        rank.sort(key=lambda x: x[0])
        employed.append(rank[0])
        cutline = employed[0][1]
        cnt = 1
        for i in range(1, len(rank)):
            if rank[i][1] < cutline:
                cnt += 1
                cutline = rank[i][1]
        print(cnt)

solve()