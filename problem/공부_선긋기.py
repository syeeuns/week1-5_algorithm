import sys
read = sys.stdin.readline

n = int(read())
line = []
for i in range(n):
    line.append(list(map(int, read().split())))
line.sort(key=lambda x: x[0])

s, e = line[0]
answer = 0

for i in range(1, n):
    # 안겹쳐질 때
    # 여태까지 구한 s,e로 answer에 더해주고, s, e 갱신해줌
    if line[i][0] > e:
        answer += e - s
        s, e = line[i]

    # 겹쳐질 때
    # 끝점이 포함되는지, 넘어가는지 체크해서 포함되면 그대로, 넘어가면 길이 갱신
    else:
        if e < line[i][1]:
            e = line[i][1]

# 마지막 segment 길이 더해줌
answer += e - s
print(answer)