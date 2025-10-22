def selection_sort(T):
    n = len(T)
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if T[j] < T[min_idx]:
                min_idx = j

        T[i], T[min_idx] = T[min_idx], T[i]
    return T
