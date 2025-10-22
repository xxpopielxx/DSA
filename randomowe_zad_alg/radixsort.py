
def counting(T, exp):
    n = len(T)
    result = [0] * n
    count = [0] * (10)

    for i in range(n):
        index = T[i] // exp
        count[index % 10] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        index = T[i] // exp
        result[count[index % 10] -1] = T[i]
        count[index % 10] -= 1
        i -= 1


    for i in range(n):
        T[i] = result[i]

def radix(T):
    maxi = max(T)

    exp = 1
    while maxi / exp >= 1:
        counting(T, exp)
        exp *= 10

    return T

T = [4,5,3,1,99,2,4]
print(radix(T))

