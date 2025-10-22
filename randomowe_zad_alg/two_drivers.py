import heapq

def Dijkstra(G, start, end, start_driver):
    n = len(G)
    distances = [[float("inf")]*2 for _ in range(n)]
    distances[start][start_driver] = 0

    Q = [(0,start,start_driver)]

    while Q:
        dist, u, driver = heapq.heappop(Q)

        if distances[u][driver] < dist:
            continue

        for v, w in G[u]:
            new_cost = dist + w if driver == 0 else dist  # Alicja jedzie, dodajemy wagę, Bob nie
            if new_cost < distances[v][1 - driver]:  # Jeżeli nowy koszt jest mniejszy
                distances[v][1 - driver] = new_cost
                heapq.heappush(Q, (new_cost, v, 1 - driver))

    return min(distances[end])

def two_drivers(G, start, end):
    return min(
        Dijkstra(G, start, end, 0),  # Alicja zaczyna
        Dijkstra(G, start, end, 1),  # Bob zaczyna
    )


