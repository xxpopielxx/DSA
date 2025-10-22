
def Euler_cycyle(G,s):
    n = len(G)
    euler = []
    index = [0]*n

    def Euler_visit(G, u):
        while index[u] < n:
            v = index[u]
            index[u] = v + 1
            if G[u][v] > 0:
                G[u][v], G[v][u] = 0, 0
                Euler_visit(G, v)
                euler.append(u)
    euler.append(s)
    Euler_visit(G, s)

    return euler


def Euler_stos(G, start):
    n = len(G)
    stack = [0]
    index = [0]*n
    result = []

    while stack:
        u = stack[-1]
        while index[u] < n and G[u][index[u]] == 0:
            index[u] += 1
        if index[u] == n:
            result.append(u)
            stack.pop()
        else:
            v = index[u]
            G[u][v], G[v][u] = 0,0
            stack.append(v)
    return result[::-1]




