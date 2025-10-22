
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

def ms(T):
    if len(T) < 2:
        return T
    mid = len(T) // 2
    left = ms(T[:mid])
    right = ms(T[mid:])
    return merge(left, right)


def snow(S):
    S = ms(S)
    S = S[::-1]
    maxi = 0
    for i in range(len(S)):
        snow_collected = S[i] - i
        if snow_collected > 0:
            maxi += snow_collected
        else:
            break
    return maxi

print(snow([1,7,3,4,1]))

