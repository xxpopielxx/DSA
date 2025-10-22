#alternatywnie można k-1 razy wywołac dijkstre i dodać do siebie
import heapq

def dijkstra(G, P):
    n = len(G)
    k = len(P)

    kontrolne = [-1 for _ in range(n)] #zapisuje sobie kolejność kontrolne[v] == indeks w P dla v
    for i in range(k):
        kontrolne[P[i]] = i

    distances = [[float("inf") for _ in range(k)] for _ in range(n)]
    visited = [[False for _ in range(k)] for _ in range(n)]


    Q = []
    start = P[0]
    heapq.heappush(Q, (0, start, 0)) #(koszt, wierzchołek, liczba kontrolnych)

    distances[start][0] = 0

    while Q:
        dist, u, i = heapq.heappop(Q)

        if visited[u][i]:
            continue
        visited[u][i] = True

        for v, w in G[u]:
            new_i = i
            if kontrolne[v] == i + 1: #jeśli indeks nowego = indeks starego + 1 no to mam nową liczbę kontrlonych
                new_i += 1

            if distances[v][new_i] > distances[u] + w:
                distances[v][new_i] = distances[u] + w
                heapq.heappush(Q, (distances[v][new_i], v, new_i))

    return distances

def robot(G, P):
    distances = dijkstra(G, P)
    return distances[P[-1]][len(P)-1] #zwracam do osattneigo z przejściem wszystkich kontrolnych
