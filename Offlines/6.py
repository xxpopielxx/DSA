
def parking(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[float("inf")] * m for _ in range(n)]

    # Initialize first row
    for j in range(m):
        dp[0][j] = abs(X[0] - Y[j]) if j == 0 else min(dp[0][j-1], abs(X[0] - Y[j]))

    for i in range(1, n):
        for j in range(i, m):
            # The parking spot for X[i] must be after the one for X[i-1]
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(X[i] - Y[j]))

    return min(dp[n-1])

