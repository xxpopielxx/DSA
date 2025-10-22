
# dp[i][e] - minimalny koszt dotarcia do i-tej planety z e paliwem w baku po przybyciu n i-ta planetę

def planets(D, C, T, E):
    n = len(D)
    dp = [[float("inf")] * (E + 1) for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        for b in range(E + 1):
            if dp[i][b] == float("inf"):
                continue

            #case 1 tankujemy od 0 do E - b ton
            for x in range(E - b + 1):
                new_b = b + x
                cost = dp[i][b] + x * C[i]
                dp[i][new_b] = min(dp[i][new_b], cost)

            #case2 teleport jeśli jest
            if b == 0 and T[i][0] != i:
                j = T[i][0]
                dp[j][0] = min(dp[j][0], dp[i][0] + T[i][1])

            #case3 lot na kolejne planety w zasięgu E
            for j in range(i+1, n):
                distance = D[j] - D[i]
                if distance > E:
                    break
                if b >= distance:
                    dp[j][b - distance] = min(dp[j][b - distance], dp[i][b])

    return min(dp[n-1])



