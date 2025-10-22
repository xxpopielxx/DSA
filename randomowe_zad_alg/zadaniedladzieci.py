def binary_search(arr, x):
    pass
#zwraca max pozycje schodka do którego dochodzisz

def func(stairs, people):
    n = len(stairs)
    m = len(people)
    tab_max = [0]*(n+1)
    tab_max[0] = stairs[0]
    for i in range(1,n):
        tab_max[i] = max(tab_max[i - 1], stairs[i])
    S = 0
    for i in range(1,m):
        is_max = binary_search(tab_max, people[i])
        S+=is_max
    return S

