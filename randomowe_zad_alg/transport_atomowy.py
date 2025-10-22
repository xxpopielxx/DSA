
def floyd_warshall(G):
    n = len(G)
    D = [row[:] for row in G]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                D[x][y] = min(D[x][y], D[x][k] + D[k][y])
    return D

def atomic_transport(G,s,t,d):
    n = len(G)
    D = floyd_warshall(G)

    for i in range(n):
        if D[s][i] > d and D[t][i] > d:
            return True
    return False