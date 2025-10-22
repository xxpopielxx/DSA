#nlogk źle to jest bo tam w poleceniu jest napisane ze struktura piwo ma zostac takze
import heapq

import heapq

def pijemy(k, PIWO):
    n = len(PIWO)
    res = [0] * n

    # Ręczne zliczanie wystąpień każdego typu piwa
    cnt = [0] * (k + 1)
    for p in PIWO:
        cnt[p] += 1

    # Sprawdzenie, czy możliwe jest ułożenie bez sąsiadujących duplikatów
    if max(cnt) > (n + 1) // 2:
        return []

    # Tworzymy kopiec z typami piwa i ich ilościami (negatywne wartości dla max-heap)
    Q = []
    for typ in range(1, k + 1):
        if cnt[typ] > 0:
            heapq.heappush(Q, (-cnt[typ], typ))

    i = 0
    while Q:
        ilosc, typ = heapq.heappop(Q)
        ilosc = -ilosc
        for _ in range(ilosc):
            if i >= n:
                i = 1  # przechodzimy na indeksy nieparzyste
            res[i] = typ
            i += 2

    # Ostateczna kontrola – czy nie ma dwóch takich samych obok siebie
    for j in range(1, n):
        if res[j] == res[j - 1]:
            return []

    return res


PIWO = [1, 2, 1, 1, 1, 3, 3, 3, 2, 3]
k = 3
print(pijemy(k,PIWO))