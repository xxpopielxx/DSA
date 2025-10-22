from kol2btesty import runtests


def min_cost(O, C, T, L):
    pairs = [(0, 0)]
    for i in range(len(O)):
        pairs.append((O[i], C[i]))
    pairs.append((L, 0))
    pairs.sort()
    n = len(pairs)

    dp = [[float("inf")] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(n):
        for j in range(2):
            for k in range(i + 1, n):
                dist = pairs[k][0] - pairs[i][0]

                if dist <= T:
                    dp[k][j] = min(dp[k][j], dp[i][j] + pairs[k][1])
                elif dist <= 2 * T and j == 0:
                    dp[k][1] = min(dp[k][1], dp[i][0] + pairs[k][1])
                else:
                    break

    return min(dp[n - 1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )