import heapq

def dijkstra(G, start, B):
    n = len(G)

    distances = [[float('inf')] * 2 for _ in range(n)]
    Q = []

    for v,w,typ in G[start]:
        distances[v][typ] = w
        heapq.heappush(Q, (w, v, typ))

    while Q:
        w, u, rail_type = heapq.heappop(Q)

        if u == B:
            return w

        if w > distances[u][rail_type]:
            continue

        for v, w2, typ2 in G[u]:
            if rail_type == typ2:
                station_cost = 5 if typ2 == 1 else 10
            else:
                station_cost = 20

            new_dist = w + w2 + station_cost
            if distances[v][typ2] > new_dist:
                distances[v][typ2] = new_dist
                heapq.heappush(Q, (distances[v][typ2], v, typ2))

    return min(distances[B])

def edges_to_list(E):
    n = 0
    for u,v,_ ,_ in E:
        n = max(n,max(u,v))
    n += 1

    G = [[] for _ in range(n)]

    for u,v,w,typ in E:
        if typ == "I":
            typ = 1
        else:
            typ = 0

        G[u].append((v,w,typ))
        G[v].append((u,w,typ))

    return G

def tory_amos(E, A, B):
    G = edges_to_list(E)
    return dijkstra(G, A, B)
