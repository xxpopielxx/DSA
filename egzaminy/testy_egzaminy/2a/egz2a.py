from egz2atesty import runtests

import heapq

def coal(A, T):
    n = len(A)
    Q = []          # (index, free_space)
    next_id = 0     # numer nowego magazynu

    for i in range(n):
        transport = A[i]
        current = []
        found = False

        # szukamy pierwszego magazynu (najmniejszy index z wolnym miejscem)
        while Q:
            index, space = heapq.heappop(Q)
            if space >= transport:
                heapq.heappush(Q, (index, space - transport))
                found = True
                if i == n - 1:
                    return index
                break
            else:
                current.append((index, space))

        # wrzucamy z powrotem te, które nie wystarczyły
        for item in current:
            heapq.heappush(Q, item)

        # jeśli żaden się nie nadał → otwieramy nowy magazyn
        if not found:
            index = next_id
            next_id += 1
            heapq.heappush(Q, (index, T - transport))
            if i == n - 1:
                return index

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )