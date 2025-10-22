#najkrótsze ściezki z 1 źródła w DAG

def DFS(G, n):
    visited = [False] * n
    sortedd = [None] * n
    k = n - 1

    def DFSvisit(G, u):
        nonlocal k
        visited[u] = True
        for v, _ in G[u]:
            if not visited[v]:
                DFSvisit(G, v)
        sortedd[k] = u
        k -= 1

    for u in range(n):
        if not visited[u]:
            DFSvisit(G, u)

    return sortedd

def Bellman_ford(G, n , sortedd):
    distance = [float("inf")] * n
    parents = [None] * n
    distance[sortedd[0]] = 0

    for u in sortedd:
        for v, w in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parents[v] = u

    return distance, parents


def zad(G):
    n = len(G)
    sortedd = DFS(G, n)

    return Bellman_ford(G, n, sortedd)


def topological_sort(G, n):
    visited = [False for _ in range(n)]
    result = []

    def dfs(u):
        visited[u] = True
        for v, _ in G[u]:
            if not visited[v]:
                dfs(v)
        result.append(u)

    for u in range(n):
        if not visited[u]:
            dfs(u)
    return result[::-1]

def zad2(G, s):
    n = len(G)
    distance = [float("inf")] * n
    parents = [None] * n
    order = topological_sort(G,n)
    distance[s] = 0

    for u in order:
        for v, w in G[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parents[v] = u
    return parents, distance




