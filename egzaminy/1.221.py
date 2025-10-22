#robot

from collections import deque

def ok(i,j,n,m,L):
    return 0 <= i < n and 0 < j < m and L[i][j] != "#"

def robot(L,A,B):
    n = len(L)
    m = len(L[0])
    A = (A[1],A[0])
    B = (B[1],B[0])
    dp = [[float("inf")] * m for _ in range(n)]

    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    Q = deque()
    Q.append((0, A, "R", A)) # czas ,punkt, kierunek w którym jest obrócony, ruch wykonany zeby dojśc do tego punktu

    while Q:
        time, point, direction, prev = Q.popleft()

        for dx,dy in moves:
            ni,nj = point[0] + dx, point[1] + dy
            if ok(ni,nj,n,m,L) and (ni,nj) != prev:
                pass


