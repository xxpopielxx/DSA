from egzP9btesty import runtests

def akademik(T):
    n = len(T)

    # największy numer pokoju
    max_room = -1
    for i in range(n):
        for room in T[i]:
            if room is not None:
                max_room = max(max_room, room)

    m = max_room + 1  # liczba pokoi
    G = [[] for _ in range(n)]  # student → pokoje

    for i in range(n):
        for room in T[i]:
            if room is not None:
                G[i].append(room)

    room_to_student = [None] * m  # przypisanie pokoju do studenta

    def dfs(student, visited):
        for room in G[student]:
            if not visited[room]:
                visited[room] = True
                if room_to_student[room] is None or dfs(room_to_student[room], visited):#jesli pusty lub da się przesunąc
                    room_to_student[room] = student
                    return True
        return False

    pleased = 0
    for student in range(n):
        visited = [False] * m
        if dfs(student, visited):
            pleased += 1

    return n - pleased

runtests ( akademik )