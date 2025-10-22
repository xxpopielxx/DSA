

def merge(left, right):
    result = []
    l,r = 0,0
    inv = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            inv += len(left) - l

    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result, inv

def ms(T):
    n = len(T)
    if n < 2:
        return T, 0
    mid = n // 2
    left, inv_left = ms(T[:mid])
    right, inv_right = ms(T[mid:])
    merged, inv_merge = merge(left,right)

    total = inv_left + inv_right + inv_merge
    return merged, total


def count_inversions(T):
    res =  ms(T)
    return res[1]
print(count_inversions([1,20,6,4,]))
