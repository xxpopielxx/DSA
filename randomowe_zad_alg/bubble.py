def bubble(T):
    N = len(T)
    for i in range(N):
        for j in range(i+1, N):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
    return T