#tak naprawde to longest increasing subsequence

def binary_search(tab,x):
    left = 0
    right = len(tab)
    while left < right:
        mid = (left + right) // 2
        if tab[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def mosty(T):
    T.sort()
    V = [v for _, v in T]

    lis = []
    for v in V:
        pos = binary_search(lis, v)
        if pos == len(lis):
            lis.append(v)
        else:
            lis[pos] = v
    return len(lis)


