def dominance(P):
    n = len(P)
    Tx = [0] * (n + 1)
    Ty = [0] * (n + 1)
    for i in range(n):
        Tx[P[i][0]] += 1  # zliczanie po X
        Ty[P[i][1]] += 1  # zliczanie po Y
    for i in range(n - 1, 0, -1):  # przekształcam tablicę zliczeń na liczbę elementów większych
        Tx[i] += Tx[i + 1]  # przekształcam po X
        Ty[i] += Ty[i + 1]  # przekształcam po Y

    wynik = Tx[P[1][0]] + Ty[P[1][1]]  # przypisuję pierwszy wynik
    for i in P:
        current = Tx[i[0]] + Ty[i[1]]
        if wynik > current:  # szukam elementu z najmniejszą liczbą elementów których nie dominuje
            wynik = current
    return n - wynik + 1

P = [(1,3),
(3,4),
(4,2),
(2,2)]

print(dominance(P))