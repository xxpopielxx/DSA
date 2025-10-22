from egz1atesty import runtests


import heapq
from math import floor

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

def Dijkstra(G, s, t):
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0

    Q = [(0,s)]

    while Q:
        u_w, u = heapq.heappop(Q)
        if u == t: break
        if u_w > distance[u]: continue

        for v,w in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heapq.heappush(Q, (distance[v], v))

    return distance

def armstrong(B, G, s, t):
    A = edges_to_list(G)
    n = len(A)
    bikes = [1] * n

    for i,p,q in B:
        cnt = p/q
        if bikes[i] > cnt:
            bikes[i] = cnt

    d1 = Dijkstra(A, s, t)
    min_cost = d1[t] #gdyby nie wsiadła na rower
    d2 = Dijkstra(A, t, s)

    for i in range(n):
        cost = d1[i] + d2[i] * bikes[i]
        if cost <  min_cost:
            min_cost = cost

    return floor(min_cost) if min_cost != float("inf") else float("inf")

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )