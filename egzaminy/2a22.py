#n^2

def coal(A, T):
    warehouses = []

    for i in range(len(A)):
        t = A[i]
        for j in range(len(warehouses)):
            if warehouses[j] + t <= T:
                warehouses[j] += t
                last_warehouse = j
                break
        else:
            # nie zmieściło się nigdzie, dodaj nowy
            warehouses.append(t)
            last_warehouse = len(warehouses) - 1

    return last_warehouse

#n^2logn gorsza
import heapq

def coal(A, T):
    heap = []               # Kopiec przechowuje (index magazynu, dostępna pojemność)
    magazyny = []           # Lista z bieżącą dostępną pojemnością magazynów
    last_warehouse = 0      # Numer kolejnego nowego magazynu

    for t in A:
        temp = []
        found = False

        # Szukamy magazynu o najniższym numerze z wystarczającą pojemnością
        while heap:
            index, available = heapq.heappop(heap)
            if available >= t:
                magazyny[index] -= t
                heapq.heappush(heap, (index, magazyny[index]))
                last_used = index
                found = True
                break
            else:
                temp.append((index, available))

        # Przywróć odłożone magazyny
        for item in temp:
            heapq.heappush(heap, item)

        # Jeśli nie znaleziono pasującego magazynu, otwórz nowy
        if not found:
            magazyny.append(T - t)
            heapq.heappush(heap, (last_warehouse, T - t))
            last_used = last_warehouse
            last_warehouse += 1

    return last_used




