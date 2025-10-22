
def dominance(P):
    n = len(P)
    Tx = [0] * (n+1)
    Ty = [0] * (n+1)

    for i in range(n): #zliczam ile punktów ma daną współrzedną na x i y
        Tx[P[i][0]] += 1
        Ty[P[i][1]] += 1

    for i in range(n-1, 0, -1):
        Tx[i] += Tx[i+1] #Tx[i] = liczba punktów z x ≥ i
        Ty[i] += Ty[i+1] #Ty[i] = liczba punktów z y ≥ i

    res = float("inf")
    for i in P: # szukam elementu z najmniejszą liczbą elementów których nie dominuje
        current = Tx[i[0]] + Ty[i[1]]
        if current < res:
            res = current

    return n - res + 1



