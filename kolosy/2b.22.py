

#n^2
def min_cost(O,C,T,L):
    m = len(O)
    tab = [(0,0)]
    for i in range(m):
        tab.append((O[i], C[i]))
    tab.append((L,0))
    n = len(tab)
    tab.sort(key = lambda x: x[0])

    dp = [[float("inf")] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(n):
        for j in range(2):
            for k in range(i+1,n):
                dist = tab[k][0] - tab[i][0]
                if dist <= T:
                    dp[k][j] = min(dp[k][j], dp[i][j] + tab[k][1]) #jade jeden dalej po prostu
                elif dist <= 2 * T and j == 0: #używam mocy jeśli moge
                    dp[k][1] = min(dp[k][1], dp[i][0] + tab[k][1])
                else:
                    break

    return min(dp[n-1])









