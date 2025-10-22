from math import log

def kurs_walut(K):
    n = len(K)
    D = [[log(K[i][j]) for j in range(n)] for i in range(n)]

    for k in range(n):
        for x in range(n):
            for y in range(n):
                D[x][y] = min(D[x][y], D[x][k] + D[k][y])

    for i in range(n):
        if D[i][i] < 0:
            return True
    return False