

def snow(S):
    n = len(S)
    S.sort()
    S = S[::-1]
    res = 0
    for i in range(n):
        snow = S[i] - i
        if snow > 0:
            res += snow
        else:
            break
        i += 1

    return res

