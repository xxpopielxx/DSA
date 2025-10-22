
def merge(left, right, i):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l][0][i] < right[r][0][i]:
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

def ms(T, i):
    if len(T) < 2:
        return T
    mid = len(T) // 2
    left = ms(T[:mid], i)
    right = ms(T[mid:], i)
    return merge(left, right, i)

def depth(L):
    n = len(L)
    res = [[[0,0],0,0,0] for _ in range(n)]
    for i in range(n):
        res[i][0] = L[i]
        res[i][1] = i

    res = ms(res, 0)
    for j in range(n):
        res[j][2] = j

    res = ms(res, 1)
    for g in range(n):
        res[g][3] = g
    mini = 0
    id = 0
    res_id = 0
    for h in range(n):
        val = res[h][2] + res[h][3]
        if val < mini:
            mini = val
            id = res[h][1]
            res_id = res[h]

    result = 0
    cnt = 0
    for i in range(n):
        if res[i][0] == L[id]:
            cnt += 1
        elif res[i][0][0] >= L[id][0] and res[i][0][1] <= L[id][1]:
            result += 1
    if cnt > 1:
        result = result + cnt - 1
    return result

L = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]


print(depth(L))

