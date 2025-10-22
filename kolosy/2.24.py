
import heapq

def edges_to_list(E):
    n = 0
    for u, v, _ in E:
        n = max(n, max(u, v))
    n += 1

    G = [[] for _ in range(n)]

    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))

    return G


def dijkstra(G, start):
    n = len(G)

    visited = [[False] * 17 for _ in range(n)]
    distances = [[float("inf")] * 17 for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start, 0))  # dist, wierzchołek, liczba godzin w trasie

    distances[start][0] = 0

    while Q:
        _, u, h = heapq.heappop(Q)

        if visited[u][h]:
            continue
        visited[u][h] = True

        for v, w in G[u]:
            cost = distances[u][h] + w
            new_h = h + w

            if new_h > 16:
                new_h = w
                cost = distances[u][h] + 8 + w

            if distances[v][new_h] > cost:
                distances[v][new_h] = cost
                heapq.heappush(Q, (distances[v][new_h], v, new_h))

    return distances


def warrior(G, s, t):
    G = edges_to_list(G)
    distances = dijkstra(G, s)
    return min(distances[t])
