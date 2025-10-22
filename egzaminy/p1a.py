
def titanic(W, M, D):
    ciag = ""
    for letter in W:
        for i in range(len(M)):
            if M[i][0] == letter:
                for l in M[i][1]:
                    ciag += l
    n = len(ciag)

    available_codes = []
    for i in D:
        available_codes.append(M[i][1])

    # dp[i] = minimalna liczba liter do zakodowania ciag[0:i]
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for code in available_codes:
            ln = len(code)
            if i >= ln:
                if code == ciag[i - ln:i]:
                    dp[i] = min(dp[i], dp[i - ln] + 1)

    return dp[n]

