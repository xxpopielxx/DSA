
#dp[i][j] - minimalny koszt połączenia wszystkich wejść od i do j

def wired(T):
    n = len(T)
    dp = [[float('inf')] * n for _ in range(n)]

    #koszt pary dla elementów obok siebie
    for i in range(n-1):
        dp[i][i + 1] = 1 + abs(T[i] - T[i + 1])

    for length in range(4, n+1, 2): #length to długość podciągu (czyli ile elementów rozpatrujemy jednocześnie)
        for i in range(n - length + 1): #n - length + 1 to liczba możliwych miejsc, w których możemy zacząć przedział tej długości
            j = i + length - 1 #koniec przedziału

            dp[i][j] = min(
                dp[i+1][j-1] + 1 + abs(T[i] - T[j]), # łącze i z j, koszt reszty mamy już zapisany w dp[i+1][j-1]
                min(dp[i][k] + dp[k+1][j] for k in range(i+1, j, 2)) #dzielimy przedział gdzieś w środku
            )

    return dp[0][n-1]





