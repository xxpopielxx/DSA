def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(T):
    n = len(T)
    if n == 0:
        return T

    buckets = [[] for _ in range(n)]
    low, high = min(T), max(T)

    if low == high:
        return T

    for num in T:
        if num == high:
            ind = n-1
        else:
            ind = int((num - low) * (n - 1) / (high - low))
        buckets[ind].append(num)

    for i in range(n):
        insertionSort(buckets[i])

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1
    return T


T = [0.11,0.15,0.05,0.81,0.77,0.01,0.01]
T1 = [3,6,9,1]


print(bucket_sort(T))
print(bucket_sort(T1))



def bucket(T):
    n = len(T)
    buckets = [[] for _ in range(n)]

    for i in T:
        buc = int(i*n)
        buckets[buc].append(i)

    for bucket in buckets:
        insertionSort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1

    return T
