
#dp[i] - najwcześniejszy moment w którym można zaczyć i-ty projekt
def topological_sort(G):
    n = len(G)

    visited = [False for _ in range(n)]
    srtd = []

    def visit(u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                visit(v)

        srtd.append(u)

    for v in range(len(G)):
        if not visited[v]:
            visit(v)

    return srtd[::-1]

def projects(n, L):
    G = [[] for _ in range(n)]
    for p, q in L:
        G[q].append(p)

    order = topological_sort(G)
    dp = [0] * n
    for u in order:
        for v in G[u]:
            dp[v] = max(dp[v], dp[u] + 1)

    return max(dp) + 1




