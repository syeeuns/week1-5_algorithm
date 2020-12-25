import sys
from collections import deque
read = sys.stdin.readline

v, e = map(int, read().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
for _ in range(e):
    start, end = map(int, read().split())
    graph[start].append(end)
    indegree[end] += 1

# indegree == 0 인 노드를 큐에 담는다
queue = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        queue.append(i)

# 큐에서 하나씩 꺼내고 꺼낸 숫자는 결과 배열에 담는다 (정렬된 결과 출력을 위해), 해당 노드에서 나가는 간선을 삭제한다.
# 그 과정에서 indegree ==0 되는 노드들은 큐에 담는다.
# 큐가 빌 때까지 반복한다
result = []
while queue:
    x = queue.popleft()
    result.append(str(x))
    for one in graph[x]:
        indegree[one] -= 1
        if indegree[one] == 0:
            queue.append(one)

print(' '.join(result))