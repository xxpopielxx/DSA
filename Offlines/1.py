
def check(T):
    checked = []
    for word in T:
        reversed = word[::-1]
        correct = min(word, reversed)
        checked.append(correct)
    return checked

def sort(T):
    if len(T) <= 1:
        return T
    mid = len(T) // 2
    left = sort(T[:mid])
    right = sort(T[mid:])
    return merge(left, right)

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

    if l < len(left):
        while l < len(left):
            result.append(left[l])
            l += 1
    else:
        while r < len(right):
            result.append(right[r])
            r += 1
    return result

def strong_string(T):
    ready = sort(check(T))
    maxi_strength = 1
    current_strength = 1

    for i in range(1, len(ready)):
        if ready[i] == ready[i - 1]:
            current_strength += 1
        else:
            if current_strength > maxi_strength:
                maxi_strength = current_strength
            current_strength = 1

    return maxi_strength