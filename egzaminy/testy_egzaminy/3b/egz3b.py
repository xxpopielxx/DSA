from egz3btesty import runtests

def maze(L):
    n = len(L)

    if L[0][0] == '#' or L[n - 1][n - 1] == '#':
        return -1

    # dp[wiersz][kolumna] przechowuje długość najdłuższej ścieżki do tej komnaty.
    dp = [[-1] * n for _ in range(n)]

    # Przechodzimy przez labirynt kolumna po kolumnie, ZACZYNAJĄC OD 0
    for k in range(n):
        from_left = [-1] * n
        down_pass = [-1] * n
        up_pass = [-1] * n

        # 1. Oblicz ścieżki "wejściowe" dla bieżącej kolumny
        if k == 0:
            # Dla pierwszej kolumny jedynym wejściem jest start (0,0) z kosztem 0
            if L[0][0] == '.':
                from_left[0] = 0
        else:
            # Dla kolejnych kolumn wejściem są ścieżki z kolumny k-1
            for w in range(n):
                if L[w][k] == '.' and dp[w][k - 1] != -1:
                    from_left[w] = 1 + dp[w][k - 1]

        # 2. Propagacja w dół w bieżącej kolumnie (k)
        for w in range(n):
            if L[w][k] == '.':
                path_from_above = -1
                if w > 0 and down_pass[w - 1] != -1:
                    path_from_above = 1 + down_pass[w - 1]
                down_pass[w] = max(from_left[w], path_from_above)

        # 3. Propagacja w górę w bieżącej kolumnie (k)
        for w in range(n - 1, -1, -1):
            if L[w][k] == '.':
                path_from_below = -1
                if w < n - 1 and up_pass[w + 1] != -1:
                    path_from_below = 1 + up_pass[w + 1]
                up_pass[w] = max(from_left[w], path_from_below)

        # 4. Zapisz ostateczny wynik dla kolumny k jako maksimum z obu przejść
        for w in range(n):
            dp[w][k] = max(down_pass[w], up_pass[w])

    return dp[n - 1][n - 1]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )