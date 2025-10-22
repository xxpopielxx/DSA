from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)

    dp = [[float("inf")] * (E + 1) for _ in
          range(n)]  # dp[i][j] - minimalny koszt znalezienia się na i-tej planecie z j
    # paliwa w baku

    dp[0][0] = 0

    for i in range(n - 1):
        for j in range(E + 1):
            if dp[i][j] == float("inf"):
                continue

            dist = D[i + 1] - D[i]
            # case1: lecę na nastepną planetę jeśli mogę
            if j >= dist and i + 1 <= n:
                dp[i + 1][j - dist] = min(dp[i + 1][j - dist], dp[i][j])

            # case2: tankuje
            if j < E:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + C[i])

            # case3: uzywam teleporta jeśli mogę
            if j == 0:
                planet, cost = T[i]
                if i == planet:
                    continue
                if planet < n:
                    dp[planet][j] = min(dp[planet][j], dp[i][j] + cost)

    return min(dp[n - 1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )