
#0(n^2) 4 testy przechodzi,reszta czsowo się wywala
def reklamy(T, S, o):
    n = len(T)
    maxi = 0
    for i in range(n):
        current_max = S[i]
        a,b = T[i]
        for j in range(i+1, n):
            a1,b1 = T[j]
            if b < a1 or a > b1:
                current_max = max(current_max, S[i] + S[j])
        maxi = max(maxi, current_max)

    return maxi







