

#nlogn
def uncool(P):
    n = len(P)
    for i in range(n):
        P[i] = (P[i][0], P[i][1], i)
    P.sort()

    max_idx = -float("inf")
    a_max = -float("inf")
    b_max = -float("inf")

    for a, b, i in P:
        if a < b_max:
            if not ((b <= b_max and a >= a_max) or (a_max >= a and b_max <= b)):
                return(max_idx, i)

        if b > b_max:
            max_idx = i
            a_max = a
            b_max = b

#n^2
def uncool1(P):
    n = len(P)
    for i in range(n):
        a,b = P[i]
        for j in range(i+1, n):
            a1,b1 = P[j]

            if b < a1 or b1 < a: #rozłączne
                continue

            if (a >= a1 and b <= b1) or (a1 >= a and b1 <= b): #zawieranie
                continue

            return (i,j)

    return None