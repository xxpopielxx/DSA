from queue import PriorityQueue

import heapq


def dijkstra(G, start):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float('inf') for _ in range(n)]
    parents = [None for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start))

    distances[start] = 0

    while Q:
        _, u = heapq.heappop(Q)

        if visited[u]:
            continue
        visited[u] = True

        for v, w in G[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                parents[v] = u
                heapq.heappush(Q, (distances[v], v))

    return distances, parents

def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def dijkstra(G, s):
    n = len(G)
    q = PriorityQueue()
    q.put((0, s))
    parent = [None] * n
    distance = [float("inf")] * n
    visited = [False] * n
    distance[s] = 0

    while not q.empty():
        dist, u = q.get()
        for v in G[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                q.put((dist + v[1], v[0]))
        visited[u] = True
    return parent, distance

def Dijkstra_matrix(G, start):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float('inf') for _ in range(n)]
    parents = [None for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start))
    distances[start] = 0

    while Q:
        _, u = heapq.heappop(Q)

        if visited[u]: continue
        visited[u] = True

        for v in range(n):
            w = G[u][v]
            if w != 0 and not visited[v]:
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                    parents[v] = u
                    heapq.heappush(Q, (distances[v], v))
    return distances

G = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5)],
    []
]

print(dijkstra(G, 0))


