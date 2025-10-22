def merge(left,right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l][0] < right[r][0]:
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
    if len(T) < 2:
        return T
    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def rank(T,i):
    sum = 0
    for j in range(i - 1, -1, -1):
        if T[j] < T[i]:
            sum += 1
    return sum

def maxrank(T):
    n = len(T)
    T2 = []
    for i in range(n):
        T2.append([T[i],i])
    T2 = merge_sort(T2)
    T2 = T2[::-1]

    maxi = 0
    ind = 0
    for i in range(len(T2)):
        temp = maxi
        maxi = max(maxi, T2[i][1] - i)
        if maxi != temp:
            ind = T2[i][1]

    return rank(T,ind)

