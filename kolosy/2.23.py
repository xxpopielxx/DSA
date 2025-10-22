#spanning tree zawsze ma V-1 krawędzi
#imo VElogE albo VE chuj wie w sumie bo raz sortuje a potem juź nie, więc chyba VE
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

    T = []
    res = 0

    for e in E:
        if find(N[e[0]]) != find(N[e[1]]):
            union(N[e[0]], N[e[1]])
            T.append(e)
            res += e[2]

    return len(T), res

def adjacency_list_to_edge_list(G):
    edges = []
    for u in range(len(G)):
        for v, weight in G[u]:
            if u < v:
                edges.append((u, v, weight))
    return edges


def beautree(G):
    n = len(G)
    E = adjacency_list_to_edge_list(G)
    e = len(E)
    E.sort(key=lambda x: x[2])

    for i in range(e - n + 1):
        size, res = kruskal(E[i:i+n-1], n)
        if size == n-1:
            return res
    return None
