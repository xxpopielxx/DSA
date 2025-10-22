
def dyrektor(G, R):
    n = len(G)

    # Tworzymy kopię G bez krawędzi z R (czyli bez remontowanych dróg)
    G_filtered = []
    for u in range(n):
        # Tworzymy nową listę sąsiedztwa dla u
        nowa_lista = []
        # Skopiuj krawędzie z G[u]
        for v in G[u]:
            nowa_lista.append(v)
        # Usuń krawędzie z R[u] (dokładnie po jednej kopii)
        for r in R[u]:
            for i in range(len(nowa_lista)):
                if nowa_lista[i] == r:
                    # usuwamy tylko jedną kopię
                    del nowa_lista[i]
                    break
        G_filtered.append(nowa_lista)

    # Implementujemy Hierholzera
    cykl = []

    def dfs(u):
        while len(G_filtered[u]) > 0:
            v = G_filtered[u][-1]
            G_filtered[u].pop()
            dfs(v)
        cykl.append(u)

    dfs(0)
    cykl.reverse()
    return cykl

