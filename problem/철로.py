import sys, heapq
read = sys.stdin.readline

n = int(read())
people = []
for i in range(n):
    people.append(list(map(int, read().rstrip().split())))
    if people[i][0] > people[i][1]:
        people[i][0], people[i][1] = people[i][1], people[i][0]
d = int(read())

people.sort(key=lambda x: (x[1], x[0]))
pq = []
answer = 0

# 도착지점 기준 선분을 옮겨가면서 가능한 사람들의 출발지점을 우선순위 큐에 담아둔다. -> 가능한 사람들의 수 == 우선순위 큐의 크기
# 다음 사람의 도착지점과 이전 사람의 출발지점 길이가 선분의 길이를 넘으면 이전 사람을 우선순위 큐에서 제거한다. -> 될 때까지 한다
# 만약 '(사람의 출발지점~도착지점 길이) > 선분의 길이' 라면 과정을 거치지 않고 넘어간다.
for i in range(n):
    if people[i][1] - people[i][0] <= d:
        heapq.heappush(pq, people[i][0])
    else: continue
    while pq:
        temp = people[i][1]
        if (temp - pq[0]) <= d: break
        else: heapq.heappop(pq)
    answer = max(answer, len(pq))

print(answer)

