def find_articulation_points(G):
    n = len(G)

    visited = [False for _ in range(n)]
    times = [float("inf") for _ in range(n)]
    lows = [float("inf") for _ in range(n)]
    parents = [None for _ in range(n)]
    articulation_points = []

    current_time = 1

    def dfs_visit(v):
        nonlocal current_time

        visited[v] = True
        times[v] = lows[v] = current_time
        current_time += 1
        children = 0

        for u in G[v]:
            if not visited[u]:
                parents[u] = v
                dfs_visit(u)
                children += 1

                lows[v] = min(lows[v], lows[u])  # dziedziczenie low od dziecka

                # Punkt artykulacji
                if parents[v] is None:
                    if children >= 2:
                        articulation_points.append(v)
                else:
                    if lows[u] >= times[v]:
                        articulation_points.append(v)

            elif u != parents[v]:  # jeśli jest krawędź, a nie jest rodzicem - to jest to krawędź wsteczna
                lows[v] = min(lows[v], times[u])

    dfs_visit(0)

    return list(set(articulation_points))



def koleje(B):
    max_index = 0
    for a,b in B:
        max_index = max(max_index, a, b)
    n = max_index + 1

    G = [[] for _ in range(n)]
    for a,b in B:
        G[a].append(b)
        G[b].append(a)

    return len(find_articulation_points(G))














