from collections import deque

def edges_to_list(E,t,px):
    n = 0
    for u,v,_ in E:
        n = max(n, max(u,v))
    n += 1

    graph = [[] for _ in range(n)]
    for u,v,p in E:
        if abs(px - p) > t:
            continue
        graph[u].append(v)
        graph[v].append(u)

    return graph

def bfs(G,x,y):
    Q = deque()
    visited = [False] * len(G)

    visited[x] = True
    Q.append(x)

    while len(Q) > 0:
        u = Q.popleft()

        for v in G[u]:
            if not visited[v]:
                if v == y: return True
                visited[v] = True
                Q.append(v)

    return False

def Flight(L,x,y,t):
    p_tab = []
    for u,v,p in L:
        if p not in p_tab:
            p_tab.append(p)

    for i in p_tab:
        G = edges_to_list(L, t, i)
        if bfs(G,x,y): return True

    p_tab_sorted = sorted(p_tab)
    for i in range(len(p_tab_sorted)-1):
        p1 = p_tab_sorted[i]
        p2 = p_tab_sorted[i+1]
        if p1 + t >= p2 - t:
            mid_p = (p1 + p2)/2
            G = edges_to_list(L,t,mid_p)
            if bfs(G,x,y): return True
    return False


from collections import deque














