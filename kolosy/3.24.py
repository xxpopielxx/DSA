

#dp[i][j] - minimalna ilość wyciętych drzew do i-tego drzewa przy reszcie j

def orchard(T, m):

    n = len(T)
    dp = [[float("inf")] * m for _ in range(n)]
    dp[0][0] = 1 # zawsze mogę wyciąc pierwsze drzewo
    dp[0][T[0] % m] = 0 # nie wycinam

    for i in range(1, n):
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1) #wycinam drzewo

            next_rest = (T[i] + j) % m #reszta która zostanie bez wycięcia drzewa
            dp[i][next_rest] = min(dp[i][next_rest], dp[i-1][j])

    return dp[n-1][0]