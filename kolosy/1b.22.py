
def str_to_list(str):
    T = [0 for _ in range(26)]

    for char in str:
        T[ord(char) - 97] += 1

    return T

def counting(T, ind, maxi):
    n = len(T)
    C = [0] * (maxi + 1)
    B = [0]*len(T)

    for i in range(n):
        C[(T[i][ind])] = C[(T[i][ind])] + 1

    for i in range(1, maxi):
        C[i] += C[i - 1]

    for i in range(n-1, -1, -1):
        B[C[(T[i][ind])] - 1] = T[i]
        C[T[i][ind]] -= 1

    for i in range(n):
        T[i] = B[i]

def radix_sort(T):
    maxChar = 0
    for i in range(26):
        for j in range(len(T)):
            if T[j][i] > maxChar:
                maxChar = T[j][i]


    for i in range(25, -1, -1):
        counting(T, i, maxChar + 1)

def f(T):
    n = len(T)

    for i in range(n):
        T[i] = str_to_list(T[i])

    radix_sort(T)

    max_ana = 1
    ana = 1
    for i in range(1,n):
        if T[i] == T[i -1]:
            ana += 1
        else:
            max_ana = max(max_ana, ana)
            ana = 1

    max_ana = max(max_ana, ana)
    return max_ana
T = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
print(f(T))
