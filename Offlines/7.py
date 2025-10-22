
# f(i, j) = minimalna liczba drzew do i-tego indeksu, jaką było trzeba wyciąć, aby mieć j-tą resztę z dzielenia przez m jabłek
def orchard(T, m):
    n = len(T)

    dp = [[n for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    dp[0][T[0] % m] = 0

    for i in range(1, n):
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1) #wycinam drzewo

            future_rest = (j + T[i]) % m
            dp[i][future_rest] = min(dp[i][future_rest], dp[i - 1][j]) #nie wycinam

    return dp[n - 1][0]





