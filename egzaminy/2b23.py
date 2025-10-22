
#dp[i][j] - minimalna suma odległości biurowców do i przy założeniu że i-ty ma przydzieloną j-tą działkę

def parking(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[float("inf")] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = abs(X[0] - Y[j]) if j == 0 else min(dp[0][j-1], abs(X[0] - Y[j]))

    for i in range(1, n):
        for j in range(i, m):
            dp[i][j] = min(dp[i][j], dp[i][j-1], dp[i-1][j-1] + abs(X[i] - Y[j]))

    return min(dp[n-1])









