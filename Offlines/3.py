from collections import deque

def bfs(G, s):
    n = len(G)
    visited = [False] * n
    visited[s] = True
    distances = [float("inf")] * n
    distances[s] = 0
    parents = [-1] * n

    queue = deque()
    queue.append(s)

    while len(queue) > 0:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)

    return visited, distances, parents

def longer(G, s, t):
    visited, distances, parents = bfs(G, s)
    distance_t1 = distances[t]
    if distance_t1 == float("inf"):
        return None

    path = []
    vertex = t
    while parents[vertex] != -1:
        path.append(parents[vertex], vertex)
        vertex = parents[vertex]

    del visited, distances, parents

    for edge in path:
        G[edge[0]].remove(edge[1])
        G[edge[1]].remove(edge[0])

        visited, distances, parents = bfs(G,s)
        distance_t2 = distances[t]
        if distance_t2 > distance_t1:
            return edge

        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])

        del visited, distances, parents

    return None


