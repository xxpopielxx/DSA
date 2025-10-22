import heapq

def goodknight(G, s, t):
    n = len(G)

    distances = [[float("inf")] * 17 for _ in range(n)]
    distances[s][0] = 0
    Q = [(0, 0, s)]

    while Q:
        dist, fatigue, u = heapq.heappop(Q)

        if dist > distances[u][fatigue]: continue

        for v in range(n):
            w = G[u][v]
            if w == -1: continue

            new_fatigue = fatigue + w
            new_dist = dist + w

            if new_fatigue > 16:
                new_fatigue = w
                new_dist += 8

            if distances[v][new_fatigue] > new_dist:
                distances[v][new_fatigue] = new_dist
                heapq.heappush(Q, (distances[v][new_fatigue], new_fatigue, v))

    return min(distances[t])

def matrix_to_adj_list(M):
    n = len(M)
    G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                G[i].append(j)

    return G






