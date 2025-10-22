
#dp[i] - maksymalna liczba sztabek do zebrania do komnaty i

def magic(C):
    n = len(C)
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        for k in range(1,4):
            current_chamber = i
            chest = C[i][0]
            next_chamber = C[i][k][1]
            cost = C[i][k][0]

            #chest - cost to ile złota zabieramy z tej skrzyni – może być ujemne (czyli dołożyliśmy).
            if next_chamber > current_chamber and dp[current_chamber] != -1 and chest - cost <= 10:
                dp[next_chamber] = max(dp[next_chamber], dp[current_chamber] + chest - cost)
                #jeśli ujemne no to nie poprawi wyniku po prostu
    return dp[-1]






