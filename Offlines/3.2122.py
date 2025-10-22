def insertion(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1

        while j >= 0 and key < T[j]:
            T[j+1] = T[j]
            j -= 1

        T[j+1] = key
    return T


def bucket(T):
    n = len(T)
    if n < 2:
        return T

    buckets = [[] for _ in range(n)]

    low, high = min(T), max(T)
    if low == high:
        return T

    for num in T:
        if num == high:
            ind = n - 1
        else:
            ind = int((num - low) * (n - 1) // (high - low))
        buckets[ind].append(num)

    for i in range(n):
        insertion(buckets[i])

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1

    return T


def SortTab(T, P):
    return bucket(T)

T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P = [(1, 5, 0.75), (4, 8, 0.25)]
print(SortTab(T, P))


