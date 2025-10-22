T = [2,8,5,3,9,1]

def heapify(T, n, i):
    l = 2*i + 1
    r = 2*i + 2
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T,n, max_ind)

def build_max_heap(T):
    n = len(T)
    for i in range((n -1)//2, - 1, -1):
        heapify(T,n,i)

def heap_sort(T):
    n = len(T)
    build_max_heap(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i,0)
    return T

print(heap_sort(T))