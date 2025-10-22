#n^2
import heapq

def dijkstra(G, start):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

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
                heapq.heappush(Q, (distances[v], v))

    return distances

def edges_to_list(E,n):
    G = [[] for _ in range(n)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    return G

def spacetravel(n, E, S, a, b):
    G  = edges_to_list(E,n)

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            u = S[i]
            v = S[j]
            G[u].append((v, 0))
            G[v].append((u, 0))

    distances = dijkstra(G, a)
    return distances[b] if distances[b] != float("inf") else None

#mlogn dodaje wirtualny wierzchołek z którym są połączone te z teleportem
import heapq

def dijkstra(G, start):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

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
                heapq.heappush(Q, (distances[v], v))

    return distances

def edges_to_list(E,n):
    G = [[] for _ in range(n)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    return G

def spacetravel(n, E, S, a, b):
    G  = edges_to_list(E,n)

    virtual = n
    G.append([])

    for u in S:
        G[u].append((virtual, 0))
        G[virtual].append((u,0))

    distances = dijkstra(G, a)
    return distances[b] if distances[b] != float("inf") else None



