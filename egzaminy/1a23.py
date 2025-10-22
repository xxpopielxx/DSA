
import heapq

def Dijkstra(G, start):
    n = len(G)
    distances = [float('inf')] * n
    parents = [None] * n

    Q = []
    heapq.heappush(Q, (0, start))  # (dystans, wierzchołek)
    distances[start] = 0

    while Q:
        dist_u, u = heapq.heappop(Q)

        if dist_u > distances[u]:
            continue

        for v, w in G[u]:
            new_dist = dist_u + w
            if distances[v] > new_dist:
                distances[v] = new_dist
                parents[v] = u
                heapq.heappush(Q, (new_dist, v))

    return distances

def Dijkstra_modified(G, start, r):
    n = len(G)
    distances = [float('inf')] * n

    Q = []
    heapq.heappush(Q, (0, start))
    distances[start] = 0

    while Q:
        dist_u, u = heapq.heappop(Q)

        if dist_u > distances[u]:
            continue

        for v, w in G[u]:
            new_w = 2 * w + r  # zmodyfikowany koszt po napadzie
            new_dist = dist_u + new_w
            if distances[v] > new_dist:
                distances[v] = new_dist
                heapq.heappush(Q, (new_dist, v))

    return distances


def gold(G,V,s,t,r):
    n = len(G)
    without_robbery = Dijkstra(G,s)
    modified_from_t = Dijkstra_modified(G,t,r)

    min_cost = float("inf")
    for i in range(n):
        cost = without_robbery[i] + modified_from_t[i] - V[i]
        min_cost = min(min_cost, cost)

    return min(min_cost, without_robbery[t])



