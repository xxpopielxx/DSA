#nk ale chyba bardziej nk^2 
#dp[i][j] = minimalny koszt dojechania do i-tej stacji z j ilością energii w baku, według testów to nie działa

def grand_prix(D,C,k,s):
    D.append(s)
    C.append(None)
    n = len(D)
    dp = [[float("inf")] * (k+1) for _ in range(n)]
    dp[0][k] = 0


    for i in range(n):
        for j in range(k+1):
            if dp[i][j] == float("inf"):
                continue

            #case1: turbo doładowanie jeśli mogę
            if j == k:
                for d in range(1,4):
                    new_i = i + d
                    if new_i >= n:
                        # można "doskoczyć" do końca trasy
                        dp[n - 1][0] = min(dp[n - 1][0], dp[i][j])
                    if new_i < n:
                        dp[new_i][0] = min(dp[new_i][0], dp[i][j])

            #case2: tankuje ileś paliwa
            available = k - j + 1
            if C[i] is not None:
                for power in range(1,available):
                    new_k = j + power
                    cost = C[i]*power
                    dp[i][new_k] = min(dp[i][new_k], dp[i][j] + cost)

            #case3: lece ile się da
            for v in range(i+1, n):
                distance = D[v] - D[i]
                if distance > j:
                    break
                dp[v][j-distance] = min(dp[v][j-distance], dp[i][j])

    return min(dp[n-1])

########################### kod Gawła
from math import inf

def miasteczko_racing(D, C, k, s):
    n = len(D)
    D = [0] + D + [s]
    C = [0] + C + [0]
    n += 2

    f = [[inf] * (k + 1) for _ in range(n)]
    f[0][k] = 0  # start z pełnym bakiem

    for i in range(n):
        for paliwo in range(k + 1):
            cost = f[i][paliwo]
            if cost == inf:
                continue

            # 1. Normalny ruch do kolejnej stacji
            if i + 1 < n:
                dist = D[i + 1] - D[i]
                if paliwo >= dist:
                    f[i + 1][paliwo - dist] = min(f[i + 1][paliwo - dist], cost)

            # 2. Tankowanie o 1 (jeśli niepełny bak)
            if paliwo < k:
                f[i][paliwo + 1] = min(f[i][paliwo + 1], cost + C[i])

            # 3. Turbo: przeskok o 1-3 stacje (tylko z pełnym bakiem)
            if paliwo == k:
                for skok in range(1, 4):
                    j = i + skok
                    if j < n:
                        f[j][0] = min(f[j][0], cost)

    return min(f[n - 1])

D = [2, 6, 8, 9, 11, 12]
C = [5, 3, 1, 4, 2, 9]
k = 5
s = 15

print(grand_prix(D,C,k,s))
