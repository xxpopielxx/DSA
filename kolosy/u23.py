
#nlogn
def ice_cream(T):
    T.sort()
    T = T[::-1]
    res = 0
    for i in range(len(T)):
        ice = T[i] - i
        if ice <= 0:
            break
        res += ice

    return res

