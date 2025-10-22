import math
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

    E.sort(key=lambda x: x[2])

    T = []

    for e in E:
        if find(N[e[0]]) != find(N[e[1]]):
            union(N[e[0]], N[e[1]])
            T.append(e)

    return T


def coords_to_edge_list(coords):
    edges = []
    n = len(coords)
    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i+1, n):
            x2, y2 = coords[j]
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            edges.append((i, j, dist))
    return edges

def mst_edge_weight_diff(mst_edges):
    if not mst_edges:
        return 0

    weights = [math.ceil(edge[2]) for edge in mst_edges]
    return max(weights) - min(weights)

def highway(A):
    edges = coords_to_edge_list(A)
    mst = kruskal(edges, len(A))

    return mst_edge_weight_diff(mst)


A =[(10,10),(15,25),(20,20),(30,40)]
print(highway(A))
