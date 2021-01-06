import sys
read = sys.stdin.readline

n = int(read())
meeting = []
for i in range(n):
    meeting.append(list(map(int, read().split())))

# 같은 endtime 에서도 정렬을 해줘야하므로 endtime으로 먼저 정렬하고, starttime으로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = meeting[0][1]
for i in range(1, len(meeting)):
    if meeting[i][0] >= end:
        cnt += 1
        end = meeting[i][1]

print(cnt)

# 같은 endtime 인거 반례 (답 3)
# 5
# 4 4
# 4 4
# 3 4
# 2 4
# 1 4