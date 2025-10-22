class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0  # wartosc krawiedzi (lewej)
        self.right = None
        self.rightval = 0  # wartos krawiedzi (prawej)
        self.x = None  # na dane pomocnicze (memoizacja)


from math import inf


def valuableTree(T, k):
    # funkcja zwraca maksymalna sume k krawedzi tworzacych spojne poddrzewo
    def dp(node, i):  # i - ile jeszcze lisci zostalo
        if node is None:  # impossible
            return -inf
        if node.left is None and node.right is None and i != 0:  # jesli mamy jescze krawedzie a brak dzieci to nie da sie juz utworzyc subtree, wiec zwracamy -inf
            return -inf
        if i == 0:  # nie mamy juz dostepnych krawedzi wiec dla noda na ktorym jestesmy zwracamy 0 bo glebiej juz nie pojdziemy
            return 0
        if node.x is not None and node.x[i] is not None:  # memoizacja jesli wynik byl juz policzony to go zwracamy
            return node.x[i]

        res = max((node.leftval + dp(node.left, i - 1)),
                  (node.rightval + dp(node.right, i - 1)))  # idziemy calkowicie w prawo lub w lewo

        for j in range(i - 1):  # idziemy j w lewo i i-2-j w prawo ( -2 bo leftval i rightval)
            res = max(res, (node.leftval + node.rightval + dp(node.left, j) + dp(node.right, i - 2 - j)))
        # memoizacja
        if node.x is None:
            node.x = [None for _ in range(k + 1)]
        node.x[i] = res
        return node.x[i]

        # szukamy maksimum po wszystkich węzłach drzewa

    sol = -inf
    stack = [T]
    while stack:
        node = stack.pop()
        sol = max(sol, dp(node, k))  # wynik dla poddrzewa z korzeniem node
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return sol


