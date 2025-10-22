import heapq

def dijkstra(G, start):
    n = len(G)

    visited = [[False] * 5 for _ in range(n)]
    distances = [[float("inf")] * 5 for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start, 0)) #dist, wierzchołek, liczba odwiedzonych atrakcji

    distances[start][0] = 0

    while Q:
        _, u, cnt = heapq.heappop(Q)

        if visited[u][cnt]:
            continue
        visited[u][cnt] = True

        for v, w in G[u]:
            if cnt + 1 <= 4:
                if distances[v][cnt + 1] > distances[u][cnt] + w:
                    distances[v][cnt + 1] = distances[u][cnt] + w
                    heapq.heappush(Q, (distances[v][cnt + 1], v, cnt + 1))

    return distances

def edges_to_list(E):
    n = 0
    for u,v,_ in E:
        n = max(n,max(u,v))
    n += 1

    G = [[] for _ in range(n)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    return G

def turysta(G, D, L):
    G = edges_to_list(G)
    distances = dijkstra(G, D)
    return distances[L][4]

