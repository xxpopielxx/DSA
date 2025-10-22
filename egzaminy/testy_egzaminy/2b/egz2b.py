from egz2btesty import runtests

def magic(C):
    n = len(C)
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        for j in range(1, 4):
            chest = C[i][0]
            current_chamber = i
            cost, next_chamber = C[i][j]

            if next_chamber > current_chamber and dp[current_chamber] != -1 and chest - cost <= 10:
                dp[next_chamber] = max(dp[next_chamber], dp[current_chamber] + (chest - cost))

    return dp[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )