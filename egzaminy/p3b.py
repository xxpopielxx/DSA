class Node:
    def __init__(self, parent, value, rank):
        self.parent = parent
        self.value = value
        self.rank = rank

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(E, p):
    N = [Node(None, v, 0) for v in range(p)]

    for i in range(p):
        N[i].parent = N[i]

    E.sort(key=lambda x: x[2], reverse = True)

    T = []

    for e in E:
        if find(N[e[0]]) != find(N[e[1]]):
            union(N[e[0]], N[e[1]])
            T.append(e)

    return T, E


def list_to_edges(G):
    E = []
    n = len(G)

    for u in range(n):
        for v, w in G[u]:
            if u < v:  # unikamy duplikatów (bo graf nieskierowany)
                E.append((u, v, w))

    return E


def lufthansa(G):
    E = list_to_edges(G)
    maxi_st, E = kruskal(E, len(G))

    suma = 0
    suma_maxi = 0
    for e in maxi_st:
        suma_maxi += e[2]

    for e in E:
        suma += e[2]

    res = suma - suma_maxi
    def find_maxi(E):
        for e in E:
            if e not in maxi_st:
                return e
    res -= find_maxi(E)[2]
    return res



