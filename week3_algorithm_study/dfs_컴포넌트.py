graph = [
    [1],
    [0, 3],
    [3],
    [1, 2],
    [6],
    [7, 8],
    [4],
    [5, 8],
    [5, 7],
    []
]

visited = [False] * 10

def dfs(graph, visited, start):
    nodes = 1
    visited[start] = True
    print(start)
    if graph[start] != []:
        for one in graph[start]:
            if not visited[one]:
                nodes += dfs(graph, visited, one)
    return nodes


def dfsALL():
    nodes = 1
    component = 0
    for i in range(len(visited)):
        if not visited[i]:
            print('new dfs start!')
            nodes = dfs(graph, visited, i)
            component += 1
            print('size : ', nodes)
    return component

print('component : ', dfsALL())
