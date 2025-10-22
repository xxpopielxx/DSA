def partition(array, p , r):
    x = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[r], array[i+1] = array[i+1], array[r]
    return i + 1

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q-1)
        quick_sort(array,q+1,r)
    return array

#QuickSort w pamięci O(logn)

def quick(A,p,r):
    while p < r:
        q = partition(A,p,r)
        if q-p < r-q:
            quick(A,p,q-1)
            p = q+1
        else:
            quick(A,q+1,r)
            r = q-1
    return A

print(quick([4,3,2,1],0,3))

#QuickSort bez rekurencji, z własnym stosem.

class Stack:
    def __init__(self):
        self.T = []
        self.size = 0

    def push(self, elem):
        self.T.append(elem)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.T.pop()

    def is_empty(self):
        return self.size == 0

def QS_iter(A,p,r):
    St = Stack()
    St.push((p,r))
    while not St.is_empty():
        a,b = St.pop()
        if b>a:
            q = partition(A,a,b)
            St.push((a,q-1))
            St.push((q+1,b))
    return A

print(QS_iter([1,4,2,8],0,3))





