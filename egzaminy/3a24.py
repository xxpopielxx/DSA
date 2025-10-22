from collections import deque
from math import inf

def modded_bfs(G, T, n):
    time = [inf] * n            # Dla każdego drzewa zapisujemy, kiedy dotarł do niego jakiś grzyb.(dążymy do jak najwcześniejszego)
    owner = [None] * n          # numer grzyba, który opanował dane drzewo
    Q = deque()

    for i in range(len(T)):
        u = T[i]
        Q.append(u)
        time[u] = 0
        owner[u] = i            # grzyb o numerze i wszczepiony do drzewa T[i]

    while Q:
        u = Q.popleft()
        t = time[u] + 1
        for v in G[u]:
            if time[v] > t:
                time[v] = t
                owner[v] = owner[u]
                Q.append(v)
            elif time[v] == t and owner[v] > owner[u]:
                owner[v] = owner[u]
                Q.append(v)

    return owner

def mykoryza(G, T, d):
    n = len(G)
    owner = modded_bfs(G, T, n)
    cnt = 0
    for g in owner:
        if g == d:
            cnt += 1
    return cnt