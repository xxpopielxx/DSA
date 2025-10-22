import heapq

def adjacency_matrix_to_list(G):
    n = len(G)
    adj_list = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] > 0:
                adj_list[u].append((v, G[u][v]))
    return adj_list

def jumper(G, s, w):
    n = len(G)
    distances = [[float("inf"), float("inf")] for _ in range(n)]
    distances[s][0] = 0
    Q = [(0,1,s)]

    while Q:
        dist, can_jump, u = heapq.heappop(Q)
        if dist > distances[u][can_jump]:
            continue

        for v, h in G[u]:
            if dist + h < distances[v][1]: #nie skoczyliśmy
                distances[v][1] = dist + h
                heapq.heappush(Q, (distances[v][1], 1, v))
            if can_jump == 1:
                for s, p in G[v]:
                    if dist + max(h,p) < distances[s][0]:
                        distances[s][0] = dist + max(h,p)
                        heapq.heappush(Q, (distances[s][0], 0, s))

    return min(distances[w][0], distances[w][1])



def jumper(G, s, w):
    n = len(G)
    distances = [[float("inf"), float("inf")] for _ in range(n)]
    distances[s][0] = 0
    Q = [(0,1,s)]

    while Q:
        dist, can_jump, u = heapq.heappop(Q)
        if dist > distances[u][can_jump]:
            continue

        for v in range(n):
            if G[u][v] == 0:
                continue
            h = G[u][v]

            if dist + h < distances[v][1]: #nie skoczyliśmy
                distances[v][1] = dist + h
                heapq.heappush(Q, (distances[v][1], 1, v))

            if can_jump == 1:
                for z in range(n):
                    if G[v][z] == 0:
                        continue

                    cost = max(h, G[v][z])
                    if dist + cost < distances[z][0]:
                        distances[z][0] = dist + cost
                        heapq.heappush(Q, (distances[z][0], 0, z))

    return min(distances[w][0], distances[w][1])


