
from heapq import heappop,heappush

def rek(T):
    n, m = len(T), len(T[0])

    def dfs(i,j):
        res = T[i][j]
        T[i][j] = 0

        if j - 1 > -1 and T[i][j - 1] != 0:
            res += dfs(i, j - 1)
        if j + 1 < m and T[i][j + 1] != 0:
            res += dfs(i, j + 1)
        if i - 1 > -1 and T[i - 1][j] != 0:
            res += dfs(i - 1, j)
        if i + 1 < n and T[i + 1][j] != 0:
            res += dfs(i + 1, j)

        return res

    for j in range(m):
        if T[0][j] != 0:
            T[0][j] = dfs(0,j)

    return T[0]

def plan(T):
    A = rek(T)
    m = len(A)

    PQ = []
    fuel = A[0] - 1
    cnt = 1
    i = 1

    while i < m-1:
        if A[i] != 0:
            heappush(PQ, -A[i])

        if fuel == 0:
            fuel += -heappop(PQ)
            cnt += 1

        i += 1
        fuel -= 1

    return cnt








