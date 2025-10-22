def sum2(T, suma):
    T = sorted(T)
    l, r = 0, len(T) - 1
    while l < r:
        if T[l] + T[r] == suma:
            return T[l],T[r]
        elif T[l] + T[r] > suma:
            r -= 1
        else:
            l += 1

T = [1,3,4,5,8,10,17]
print(sum2(T, 14))
