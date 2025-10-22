def matrix_to_adj_list(M):
    n = len(M)
    G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] != -1 and i < j:
                G[i].append((j, M[i][j]))
                G[j].append((i, M[i][j]))

    return G

import heapq

def dijkstra(G, start):
    n = len(G)

    visited = [[False] * 17 for _ in range(n)]
    distances = [[float("inf")] * 17 for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start, 0)) # distance, vertex, hours in journey

    distances[start][0] = 0

    while Q:
        dist, u, h = heapq.heappop(Q)

        if visited[u][h]:
            continue
        visited[u][h] = True

        for v, w in G[u]:
            if h + w > 16:
                cost = dist + w + 8
                new_h = w
            else:
                cost = dist + w
                new_h = h + w

            if distances[v][new_h] > cost:
                distances[v][new_h] = cost
                heapq.heappush(Q, (distances[v][new_h], v, new_h))

    return distances

def goodknight(G, s, t):
    G = matrix_to_adj_list(G)
    distances = dijkstra(G, s)
    return min(distances[t])


