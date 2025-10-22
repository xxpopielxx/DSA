from zad6testy import runtests

import heapq

def matrix_to_adj_list(M):
    n = len(M)
    G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] != 0 and i < j:
                G[i].append((j, M[i][j]))
                G[j].append((i, M[i][j]))

    return G

def dijkstra(G, start):
    n = len(G)

    distances = [[float("inf"),float("inf")] for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start, 0)) #dist, wierzchołek, dwumilowe_buty

    distances[start][0] = 0

    while Q:
        dist, u, shoes = heapq.heappop(Q)

        if dist > distances[u][shoes]:
            continue

        for v, w in G[u]:

            if shoes == 0:
                for y, w1 in G[v]:
                    shoe_dist = max(w, w1)
                    if distances[y][1] > distances[u][0] + shoe_dist:
                        distances[y][1] = distances[u][0] + shoe_dist
                        heapq.heappush(Q, (distances[y][1], y, 1))


            if distances[v][0] > distances[u][shoes] + w:
                distances[v][0] = distances[u][shoes] + w
                heapq.heappush(Q, (distances[v][0], v, 0))


    return distances

def jumper(G,s,w):
    G = matrix_to_adj_list(G)
    distances = dijkstra(G,s)
    return min(distances[w])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )