def quick_select(T, k):
    k = len(T) - k
    l, r = 0, len(T) - 1

    while l <= r:
        pivot = T[r]
        p = l

        for i in range(l, r):
            if T[i] <= pivot:
                T[p], T[i] = T[i], T[p]
                p += 1
        T[p], T[r] = T[r], T[p]

        if p > k:
            r = p - 1
        elif p < k:
            l = p + 1
        else:
            return T[p]


T = [4,8,5,2,1]
print(quick_select(T,3))