T = [4,7,1,3,9,4]
def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result

def merge_sort(T):
    n = len(T)
    if n < 2:
        return T
    mid = n // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def insertion(T):
    n = len(T)

    for i in range(1, n):
        key = T[i]
        j = i - 1

        while j >= 0 and key < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

    return T

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
        insertion(buckets[i])

    index = 0
    for bucket in buckets:
        for num in bucket:
            T[index] = num
            index += 1
    return T

def selection_sort(T):
    n = len(T)
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if T[j] < T[min_idx]:
                min_idx = j

        T[i], T[min_idx] = T[min_idx], T[i]
    return T


def counting(T, exp):
    n = len(T)
    result = [0] * n
    count = [0] * (10)

    for i in range(n):
        index = T[i] // exp
        count[index % 10] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = T[i] // exp
        result[count[index % 10] -1] = T[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        T[i] = result[i]

def radix(T):
    maxi = max(T)

    exp = 1
    while maxi / exp >= 1:
        counting(T, exp)
        exp *= 10

    return T
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

print(quick_select(T, 3))
print(radix(T))
print(selection_sort(T))
print(bucket_sort(T))
print(insertion(T))
print(merge_sort(T))

