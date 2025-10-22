def maze(L):
    n = len(L)
    prev = [-1] * n

    for i in range(n): # uzupelnienie pierwszej kolumny
        if L[i][0] == '#': break
        prev[i] = i

    down = [-1] * n # tablice pomocnicze dla kazdej z kolumn
    up = [-1] * n

    for j in range(1, n):
        down[0] = prev[0] + 1 if L[0][j] != '#' and prev[0] != -1 else -1

        for i in range(1, n): # przebiega w dol
            if L[i][j] != '#':
                tmp_val = -1
                a = prev[i]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                a = down[i - 1]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                down[i] = tmp_val
            else: down[i] = -1

        up[n - 1] = prev[n - 1] + 1 if L[n - 1][j] != '#' and prev[n - 1] != -1 else -1

        for i in range(n - 2, -1, -1): # przebiega w gore
            if L[i][j] != '#':
                tmp_val = -1
                a = prev[i]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                a = up[i + 1]
                if a != -1:
                    a += 1
                    if a > tmp_val: tmp_val = a
                up[i] = tmp_val
            else: up[i] = -1

        for i in range(n):
            prev[i] = down[i] if down[i] > up[i] else up[i]

    return prev[n - 1]






