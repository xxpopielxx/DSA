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

def quickselect(T,k):
    n = len(T)
    p, r = 0, n - 1

    while p <= r:
        x = T[r]
        i = p-1

        for j in range(p,r):
            if T[j] <= x:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i+1], T[r] = T[r], T[i+1]

        if i+1 > k:
            r = i
        elif i+1 < k:
            p = i+1
        else:
            return T[i+1]

def ksum(T, k, p):
    n = len(T)
    ksuma = 0
    for i in range(n - p + 1):
        temp = T[i:i+p]
        ksuma += quickselect(temp,len(T) - k)
    return ksuma






T = [7,9,1,5,8,6,2,12]
print(ksum(T,4, 5))