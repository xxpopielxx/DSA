from egz3atesty import runtests


def snow(T, I):
    res = []
    for a,b in I:
        res.append((a,1))
        res.append((b+1,-1))
    res.sort()

    maxi = 0
    current = 0
    for point, change in res:
        current += change
        maxi = max(maxi, current)

    return maxi


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

