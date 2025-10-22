
#0(n^2) przechodzi 6 testów czasowo sie potem wywala
def ogrod(S, V):
    n = len(S)
    m = len(V)
    maxi = 0

    for i in range(n):
        visited = [[False,False] for _ in range(m+1)]
        current_sum = V[S[i]-1]
        visited[S[i]][0] = True
        for j in range(i+1,n):
            if not visited[S[j]][0]: #jeśli jescze nie było tego gatunku
                current_sum += V[S[j]-1] #dodaje do sumy
                visited[S[j]][0] = True #ustawiam że ten gatunek już był

            elif not visited[S[j]][1]: #jeśli już był ten gatunek
                current_sum -= V[S[j]-1] #odejmuje raz
                visited[S[j]][1] = True #ustawiam że już odjąłem to co wcześniej dodałem i zaznaczam że już odjąłem

            maxi = max(maxi, current_sum) #aktualizuje maxi

    return maxi


def ogrod1(S, V):
    pass





