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
    if len(T) < 2:
        return T
    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)



T = [3,6,1,2,5,8]
print(merge_sort(T))