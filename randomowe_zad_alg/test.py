#leetcode 857. Minimum Cost to Hire K Workers

import heapq

def mincostToHireWorkers(quality, wage, k):
    pairs = []
    n = len(wage)
    for i in range(n):
        pairs.append((wage[i] / quality[i], quality[i]))
    pairs.sort()

    heap = []
    res = float("inf")
    current = 0

    for efficiency, quality in pairs:
        heapq.heappush(heap, -quality)
        current += quality
        if len(heap) > k:
            current += heapq.heappop(heap)
        if len(heap) == k:
            res = min(res, current * efficiency)

    return res

quality = [10, 20, 5]

wage = [70, 50, 30]

k = 2

print(mincostToHireWorkers(quality, wage, k))


# 1326. Minimum Number of Taps to Open to Water a Garden

def minTaps(n , ranges):
    pairs = []
    for i in range(len(ranges)):
        left = max(0, i - ranges[i])
        right = min(n, i + ranges[i])
        pairs.append((left, right))
    pairs.sort()

    if not pairs or pairs[0][0] > 0:
        return -1

    res = 0
    current_end = 0
    max_reach = 0
    i = 0

    while current_end < n:
        found = False
        while i < len(pairs) and pairs[i][0] <= current_end:
            max_reach = max(max_reach, pairs[i][1])
            i += 1
            found = True

        if not found:
            return -1

        current_end = max_reach
        res += 1

    return res

n = 5
ranges = [3,4,1,1,0,0]

print(minTaps(n, ranges))


# 630. Course Schedule III
def scheduleCourse(courses):
    courses.sort(key = lambda x: x[1])
    heap = []

    total_days = 0
    for duration, lastday in courses:
        total_days += duration
        heapq.heappush(heap, -duration)

        if total_days > lastday:
            longest = -heapq.heappop(heap)
            total_days -= longest

    return len(heap)


courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]

print(scheduleCourse(courses))


# egz1a 23/24

def edges_to_list(E):
    n = 0
    for u,v,_ in E:
        n = max(n,max(u,v))
    n += 1

    G = [[] for _ in range(n)]

    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    return G

import heapq

def dijkstra(G, start):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start))

    distances[start] = 0

    while Q:
        _, u = heapq.heappop(Q)

        if visited[u]:
            continue
        visited[u] = True

        for v, w in G[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                heapq.heappush(Q, (distances[v], v))

    return distances

def armstrong(B, G, s, t):
    G = edges_to_list(G)
    n = len(G)
    bikes = [1] * n

    for vertex, p, q in B:
        efficiency = p/q
        if efficiency < bikes[vertex]:
            bikes[vertex] = efficiency

    dijkstra_s = dijkstra(G, s)
    dijkstra_t = dijkstra(G, t)

    mini = float("inf")
    for i in range(n):
        res = dijkstra_s[i] + dijkstra_t[i] * bikes[i]
        mini = min(mini, res)

    return mini



# egz 1b 23/24

def kstrong(T, k):
  n = len(T)
  dp = [[-float("inf")] * (k + 1) for _ in range(n)]  # dp[i][j] - maksymalna suma do i-tego indeksu z j usunięciamy j <= k
  for i in range(k + 1):
    dp[0][i] = T[0] if T[0] > 0 else 0

  maxi = T[0]
  for i in range(1, n):
    for j in range(k + 1):
      # case1 zaczynam nowy podciąg
      dp[i][0] = max(dp[i][0], T[i])

      # case2 kontynuje stary podciąg nie usuwając i-tego elementu
      dp[i][j] = max(dp[i][j], dp[i - 1][j] + T[i])

      # case3 kontynuje stary podciąg usuwając i-ty element
      if j-1 > -1:
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

      maxi = max(maxi, dp[i][j])
  return maxi

# egz 2a 23/24

def wired(T):
    n = len(T)
    dp = [[float("inf")] * n for _ in range(n)] # minimalny koszt połączenia wszystkich wejść od i do j
    for i in range(n-1):
        dp[i][i+1] = 1 + abs(T[i] - T[i+1])

    for length in range(4, n+1, 2):
        for i in range(n - length + 1): #początek przedziału
            j = i + length - 1 #koniec przedziału

            dp[i][j] = min(dp[i][j],
                dp[i+1][j-1] + 1 + abs(T[i] - T[j]), #łącze i-ty z j-tym
                min(dp[i][k] + dp[k+1][j] for k in range(i+1,j,2))
            )
    return dp[0][n-1]


# egz 2b 23/24

import heapq

def dijkstra(G, start, B):
    n = len(G)

    distances = [[float('inf')] * 2 for _ in range(n)]
    Q = []

    for v,w,typ in G[start]:
        distances[v][typ] = w
        heapq.heappush(Q, (w, v, typ))

    while Q:
        w, u, rail_type = heapq.heappop(Q)

        if u == B:
            return w

        if w > distances[u][rail_type]:
            continue

        for v, w2, typ2 in G[u]:
            if rail_type == typ2:
                station_cost = 5 if typ2 == 1 else 10
            else:
                station_cost = 20

            new_dist = w + w2 + station_cost
            if distances[v][typ2] > new_dist:
                distances[v][typ2] = new_dist
                heapq.heappush(Q, (distances[v][typ2], v, typ2))

    return min(distances[B])

def edges_to_list(E):
    n = 0
    for u,v,_ ,_ in E:
        n = max(n,max(u,v))
    n += 1

    G = [[] for _ in range(n)]

    for u,v,w,typ in E:
        if typ == "I":
            typ = 1
        else:
            typ = 0

        G[u].append((v,w,typ))
        G[v].append((u,w,typ))

    return G

def tory_amos(E, A, B):
    G = edges_to_list(E)
    return dijkstra(G, A, B)


# egz 3a 23/24

from collections import deque
def bfs(G, T):
    n = len(G)

    owners = [-1 for _ in range(n)]
    times = [float("inf") for _ in range(n)]

    Q = deque()

    for i in range(len(T)):
        times[T[i]] = 0
        owners[T[i]] = i
        Q.append((T[i], i, 0))

    while Q:
        tree, fungus, time = Q.popleft()
        arrival_time = time + 1
        for v in G[tree]:
                if times[v] > arrival_time:
                    times[v] = arrival_time
                    owners[v] = fungus
                    Q.append((v, fungus, arrival_time))
                elif times[v] == arrival_time and fungus < owners[v]:
                    owners[v] = fungus
                    Q.append((v, fungus, arrival_time))


    return owners

def mykoryza(G, T, d):
    owners = bfs(G, T)
    res = 0
    for i in range(len(owners)):
        if owners[i] == d:
            res += 1

    return res

# egz 3b 23/24

def generate(k, n):
    res = [False] * (n + 1)
    i = 1
    x = k
    while x <= n:
        res[x] = True
        x = x + (x % i) + 7
        i += 1
    return res

def kunlucky(T, k):
    n = len(T)
    tab = generate(k, n)

    i, j = 0, 0
    res = 0
    cnt = 0

    while j < n:
        num = T[j]
        if tab[num]:
            cnt += 1


        while cnt > 2:
            num1 = T[i]
            if tab[num1]:
                cnt -= 1
            i += 1

        res = max(res, j - i + 1)
        j += 1
    return res


# egz 1a 22/23

import heapq

def dijkstra(G, start):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start))

    distances[start] = 0

    while Q:
        _ , u = heapq.heappop(Q)

        if visited[u]:
            continue
        visited[u] = True

        for v, w in G[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                heapq.heappush(Q, (distances[v], v))

    return distances


def dijkstra_mod(G, start, r):
    n = len(G)

    visited = [False for _ in range(n)]
    distances = [float("inf") for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start))

    distances[start] = 0

    while Q:
        _, u = heapq.heappop(Q)

        if visited[u]:
            continue
        visited[u] = True

        for v, w in G[u]:
            if distances[v] > distances[u] + 2*w + r:
                distances[v] = distances[u] + 2*w + r
                heapq.heappush(Q, (distances[v], v))

    return distances

def gold(G, V, s, t, r):
    d_before = dijkstra(G, s)
    d_after = dijkstra_mod(G, t, r)

    res = float("inf")
    for i in range(len(G)):
        res = min(res, d_before[i] + d_after[i] - V[i])

    return res



# egz 1b 22/23

def planets(D, C, T, E):
    n = len(D)

    dp = [[float("inf")] * (E+1) for _ in range(n)] #dp[i][j] - minimalny koszt znalezienia się na i-tej planecie z j
    # paliwa w baku

    dp[0][0] = 0

    for i in range(n-1):
        for j in range(E+1):
            if dp[i][j] == float("inf"):
                continue

            dist = D[i+1] - D[i]
            #case1: lecę na nastepną planetę jeśli mogę
            if j >= dist and i+1 <= n:
                dp[i+1][j - dist] = min(dp[i+1][j - dist], dp[i][j])

            #case2: tankuje
            if j < E:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + C[i])

            #case3: uzywam teleporta jeśli mogę
            if j == 0:
                planet, cost = T[i]
                if i == planet:
                    continue
                if planet < n:
                    dp[planet][j] = min(dp[planet][j], dp[i][j] + cost)


    return min(dp[n-1])



# egz 2a 22/23

def dominance(P):
    n = len(P)
    x_tab = [0] * n
    y_tab = [0] * n

    for i in range(n):
        x_tab[P[i][0]] += 1
        y_tab[P[i][1]] += 1


    for i in range(n-1, 0, -1):
        x_tab[i] += x_tab[i+1]
        y_tab[i] += y_tab[i+1]

    res = -float("inf")
    for i in range(n):
        x, y = P[i]
        curr = x_tab[x]+ y_tab[y]
        if curr > res:
            res = curr

    return n - res + 1

# egz 2b 22/23

def parking(X, Y):
  n, m = len(X), len(Y)
  dp = [[float("inf")] * m for _ in range(n)]  # minimalna suma do i-tego wieżowaca z założeniem że i jest połączone z j

  for j in range(m):
    dp[0][j] = abs(X[0] - Y[j]) if j == 0 else min(dp[0][j - 1], abs(X[0] - Y[j]))

  for i in range(1, n):
    for j in range(i,m):
      dp[i][j] = min(dp[i][j], dp[i  - 1][j - 1] + abs(X[i] - Y[j]), dp[i][j-1])

  return min(dp[n - 1])


# egz 3a 22/23

def matrix_to_adj_list(M):
    n = len(M)
    G = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] != -1 and i < j:
                G[i].append((j, M[i][j]))
                G[j].append((i, M[i][j]))

    return G

import heapq

def dijkstra_state(G, start):
    n = len(G)

    visited = [[False]* 17 for _ in range(n)]
    distances = [[float("inf")] * 17 for _ in range(n)]

    Q = []
    heapq.heappush(Q, (0, start, 0)) # dist, vertex, hours

    distances[start][0] = 0

    while Q:
        dist, u, hours = heapq.heappop(Q)

        if visited[u][hours]:
            continue
        visited[u][hours] = True

        for v, w in G[u]:
            new_hours = hours + w
            new_dist = dist + w

            if new_hours > 16:
                new_hours = w
                new_dist = dist + w + 8

            if distances[v][new_hours] > new_dist:
                distances[v][new_hours] = new_dist
                heapq.heappush(Q, (distances[v][new_hours], v, new_hours))

    return distances

def goodknight(G, s, t):
    G = matrix_to_adj_list(G)
    distances = dijkstra_state(G, s)
    return min(distances[t])


#egz 3b 22/23

def uncool(P):
    tab = []
    for i in range(len(P)):
        a, b = P[i]
        tab.append((a, b, i))

    tab.sort()

    max_idx = -float("inf")
    a_max = -float("inf")
    b_max = -float("inf")

    for a, b, i in tab:
        if a < b_max:
            if not ((b <= b_max and a >= a_max) or (a_max >= a and b_max <= b)):
                return (max_idx, i)

        if b > b_max:
            max_idx = i
            a_max = a
            b_max = b


# egz 1a 21/22
def snow(S):
    S.sort(reverse = True)
    i = 0
    res = 0
    for j in range(len(S)):
        profit = S[j] - i
        if profit > 0:
            res += S[j] - i
    return res

# egz 2a 21/22

#n^2
def coal_n2(A, T):
    storage = []
    for i in range(len(A)):
        transport = A[i]
        found = False
        for j in range(len(storage)):
            if transport <= storage[j]:
                storage[j] -= transport
                if i == n-1:
                    return j
                found = True

        if not found:
            storage.append(T-transport)
            if i == n-1:
                return len(storage) - 1

#n^2logn także gorsza
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


# egz 2b 21/22

def magic(C):
    n = len(C)
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        for j in range(1, 4):
            chest = C[i][0]
            current_chamber = i
            cost, next_chamber = C[i][j]

            if next_chamber > current_chamber and dp[current_chamber] != -1 and chest - cost <= 10:
                dp[next_chamber] = max(dp[next_chamber], dp[current_chamber] + (chest - cost))

    return dp[n-1]

# egz 3a 21/22

def snow(T, I):
    res = []
    for a,b in I:
        res.append((a,1))
        res.append((b+1,-1))
    res.sort()

    maxi = 0
    current = 0
    for point, change in res:
        current += change
        maxi = max(maxi, current)

    return maxi

# kol 3 23/24

def orchard(T, m):
    n = len(T)
    dp = [[float("inf")] * m for _ in range(n)] #dp[i][j] mini. liczba wyciętych drzew do i-tego drzewa z resztą z dzielenia j
    dp[0][0] = 1
    dp[0][T[0] % m] = 0

    for i in range(1, n):
        for j in range(m):

            #case1 wycinam i-te drzewo
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)

            #case2 nie wycinam i-tego drzewa
            next_rest = (T[i] + j) % m
            dp[i][next_rest] = min(dp[i][next_rest], dp[i-1][j])

    return dp[n-1][0]


# kolu 23/24

def topological_sort(G):
    n = len(G)

    visited = [False for _ in range(n)]
    srtd = []

    def visit(u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                visit(v)

        srtd.append(u)

    for v in range(len(G)):
        if not visited[v]:
            visit(v)

    return srtd[::-1]

def edges_to_list(E, n):
    G = [[] for _ in range(n)]

    for u,v in E:
        G[v].append(u)

    return G

def projects(n, L):
    G = edges_to_list(L)
    srtd = topological_sort(G)

    visited = [False for _ in range(n)]

    cnt = 0
    def visit(u):
        nonlocal cnt
        visited[u] = True
        cnt += 1
        for v in G[u]:
            if not visited[v]:
                visit(v)

    visit(srtd[0])
    return cnt + 1


# kol2 22/23

class Node:
    def __init__(self, parent, value, rank):
        self.parent = parent
        self.value = value
        self.rank = rank

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(E, p):
    N = [Node(None, v, 0) for v in range(p)]

    for i in range(p):
        N[i].parent = N[i]

    T = []
    res = 0
    for e in E:
        if find(N[e[0]]) != find(N[e[1]]):
            union(N[e[0]], N[e[1]])
            T.append(e)
            res += e[2]

    return len(T), res


def adjacency_list_to_edges(G):
    edges = []
    for u in range(len(G)):
        for v, w in G[u]:
            if u < v:
                edges.append((u, v, w))
    return edges

def beautree(G):
    n = len(G)
    E = adjacency_list_to_edges(G)
    E.sort(key = lambda x: x[2])
    m = len(E)

    for i in range(m - n + 1):
        size, res = kruskal(E[i: i + n - 1], n)
        if size == n - 1:
            return res
    return None

# kolu 22/23
#nlogn

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
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

def merge_sort(T):
    if len(T) < 2:
        return T
    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def ice_cream(T):
    T = merge_sort(T)
    T = T[::-1]
    res = 0
    for i in range(len(T)):
        add = T[i] - i
        if add > 0:
            res += add

    return res

#n + max(T)
def ice_cream(T):
    if not T:
        return 0

    max_T = max(T)
    count = [0] * (max_T + 1)

    # histogram
    for v in T:
        count[v] += 1

    total = 0
    minute = 0  # ile kubełków już zjedliśmy

    # od największej objętości w dół
    for v in range(max_T, -1, -1):
        while count[v] > 0:
            remaining = v - minute
            if remaining <= 0:
                return total
            total += remaining
            minute += 1
            count[v] -= 1

    return total


# kol 2b 21/22

def min_cost(O,C,T,L):
    pairs = [(0,0)]
    for i in range(len(O)):
        pairs.append((O[i], C[i]))
    pairs.append((L, 0))
    pairs.sort()
    n = len(pairs)

    dp = [[float("inf")] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(n):
        for j in range(2):
            for k in range(i+1, n):
                dist = pairs[k][0] - pairs[i][0]

                if dist <= T:
                    dp[k][j] = min(dp[k][j], dp[i][j] + pairs[k][1])
                elif dist <= 2*T and j == 0:
                    dp[k][1] = min(dp[k][1], dp[i][0] + pairs[k][1])
                else:
                    break

    return min(dp[n-1])










































