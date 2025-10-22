import heapq
import math
def dijkstra(G, start, OD, B,t):
    n = len(G)

    distances = [(float("inf"), float("inf")) for _ in range(n)] #dist, number of bottles

    Q = []
    heapq.heappush(Q, (0, 1, start, B)) # (total_time, bottles_used, current_stop, remaining_water)

    distances[start] = (0, 1)

    while Q:
        current_time, bottles, u, remaining = heapq.heappop(Q)

        if u == t: #jeśli doszedłem zwracam
            return bottles
        if current_time > distances[u][0]: #jeśli nie opłaca się sprawdzać: continue
            continue

        for v, travel_time in G[u]:
            if current_time % OD[u] == 0: #jeśli czs oczekiwania 0, to czs odjazdu jest równy czasowi current
                departure_time = current_time
            else:
                departure_time = ((current_time // OD[u]) + 1) * OD[u] #jeśli nie 0 to pierwsza większa wielokrotność OD[u] >
                #od current_time

            waiting = departure_time - current_time #ile czasu oczekiwania na przystanku
            total_time = waiting + travel_time  #czas podrózy do kolejnego wliczając czas oczekiwania

            if remaining >= total_time: #jeśli starczy wody no to git
                new_remaining = remaining - total_time
                new_bottles = bottles
            else: #jeśli nie starczy to kupuje nową butelkę
                new_bottles = bottles + 1
                new_remaining = B - total_time

            arrival_time = current_time + total_time #obliczam czas przyjazdu
            #jesli sie opłaca to aktualizuje distances
            if arrival_time < distances[v][0] or (arrival_time == distances[v][0] and new_bottles < distances[v][1]):
                distances[v] = (arrival_time, new_bottles)
                heapq.heappush(Q,(arrival_time, new_bottles, v, new_remaining))

    return -1

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

def abus(KR, OD, B, s, t):
    G = edges_to_list(KR)
    return dijkstra(G, s, OD, B,t)



####################################################

import heapq
import math
def dijkstra(G, start, OD, B,t):
    n = len(G)

    distances = [(float("inf"), float("inf")) for _ in range(n)] #dist, number of bottles

    Q = []
    heapq.heappush(Q, (0, 1, start, B)) # (total_time, bottles_used, current_stop, remaining_water)

    distances[start] = (0, 1)

    while Q:
        current_time, bottles, u, remaining = heapq.heappop(Q)

        if u == t: #jeśli doszedłem zwracam
            return bottles
        if current_time > distances[u][0] or (current_time == distances[u][0] and bottles > distances[u][1]):
            continue

        for v, travel_time in G[u]:
            if current_time % OD[u] == 0: #jeśli czs oczekiwania 0, to czs odjazdu jest równy czasowi current
                departure_time = current_time
                waiting = 0
            else:
                departure_time = ((current_time // OD[u]) + 1) * OD[u] #jeśli nie 0 to pierwsza większa wielokrotność OD[u] >
                #od current_time
                waiting = departure_time - current_time

            total_time = waiting + travel_time  #czas podrózy do kolejnego wliczając czas oczekiwania

            if remaining >= total_time: #jeśli starczy wody no to git
                new_remaining = remaining - total_time
                new_bottles = bottles
            else: #jeśli nie starczy to kupuje nową butelkę
                new_bottles = bottles + 1
                new_remaining = B - total_time

            arrival_time = current_time + total_time #obliczam czas przyjazdu
            #jesli sie opłaca to aktualizuje distances
            if arrival_time < distances[v][0] or (arrival_time == distances[v][0] and new_bottles < distances[v][1]):
                distances[v] = (arrival_time, new_bottles)
                heapq.heappush(Q,(arrival_time, new_bottles, v, new_remaining))

    return -1

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

def abus(KR, OD, B, s, t):
    G = edges_to_list(KR)
    return dijkstra(G, s, OD, B,t)

KR = [(0, 4, 4), (0, 1, 7), (1, 3, 6), (4, 3, 2), (1, 2, 1), (3, 2, 3)]
OD = [1, 6, 1, 7, 4]
B = 10
s = 0
t = 2

print(abus(KR, OD, B, s, t))