
#dp[i][j] - maksymalna suma do itego indeksu z najwyżej j usunięciami j <= k

def kstrong(T, k):
    n = len(T)

    dp  = [[-float("inf")] * (k+1) for _ in range(n)]
    for i in range(k + 1):
        dp[0][i] = T[0] if T[0] > 0 else 0

    maxi = T[0]
    for i in range(1, n):
        for j in range(k+1):
            #case1: zaczynam nowy podciąg
            dp[i][j] = max(dp[i][j], T[i])

            #case2: usuwam i-ty wyraz
            if j-1 > -1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1])

            #case3: nie usuwam
            dp[i][j] = max(dp[i][j], dp[i-1][j] + T[i])

        maxi = max(maxi, dp[i][j])

    return maxi










