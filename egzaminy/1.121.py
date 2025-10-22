
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket(T):
    n = len(T)
    buckets = [[] for _ in range(n)]

    for i in T:
        buc = int(i[0]*n)
        buckets[buc].append(i)

    for bucket in buckets:
        insertionSort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1

    return T

def bucket_sort(T):
    n = len(T)
    if n == 0:
        return T

    buckets = [[] for _ in range(n)]
    low, high = T[0][0], T[0][0]

    for i in T:
        if i[0] < low:
            low = i[0]
        elif i[0] > high:
            high = i[0]

    if low == high:
        return T

    for num in T:
        val = num[0]
        if val == high:
            ind = n-1
        else:
            ind = int((val - low) * (n - 1) / (high - low))
        buckets[ind].append(num)

    for i in range(n):
        insertionSort(buckets[i])

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1
    return T

#do tego ten zmodyfikowany O(nlogn)
def chaos_index1(T):
    for i in range(len(T)):
        T[i] = (T[i], i)
    T = bucket_sort(T)
    maxi = 0
    for i in range(len(T)):
        current = abs(i - T[i][1])
        maxi = max(maxi, current)
    return maxi

#do tego zwykły bucket O(n^2)
def chaos_index(T):
    G = []
    for val in T:
        G.append(val)
    G = bucket_sort(G)
    maxi = 0
    for i in range(len(T)):
        value = T[i]
        for j in range(len(G)):
            if value == G[j]:
                maxi = max(maxi, abs(i - j))
    return maxi

