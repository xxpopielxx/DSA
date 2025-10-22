from heapq import heappop, heappush


def adjacency_list(n, E, S):
    G = [[] for _ in range(n)]

    for v,u,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    for i in range(len(S) - 1):
        G[S[i]].append((S[i+1], 0))
        G[S[i+1]].append((S[i], 0))

    return G


def Dijkstra(G, a, b, n):
    distance = [float("inf")] * n
    distance[a] = 0
    PQ = [(0, a)]

    while len(PQ) > 0:
        u_w, u = heappop(PQ)

        if u == b: break
        if u_w > distance[u]: continue

        for v, w in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heappush(PQ, (distance[v], v))

        return distance[b]

def spacetravel(n, E, S, a, b):
    G = adjacency_list(n, E, S)
    res = Dijkstra(G, a, b, n)
    return res if res != float("inf") else None
