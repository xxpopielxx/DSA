
#dp[i][j][k] - minimalna liczba skoków do dotarcia do punktu [i][j] gdy k = 0,1, 0 czyli nie prebilimsy sie jescze,
# czyli przebilismy już ścianę
#n^2
from collections import deque

def kurt(D):
    n = len(D)
    dp = [[[float("inf")] * 2 for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = 0
    moves = ((1,0), (-1,0), (0,1), (0,-1))

    Q = deque()
    dp[0][0][0] = 0
    Q.append((0,0,0)) #i,j,przebil

    while Q:
        i,j,przebil = Q.popleft()
        time = dp[i][j][przebil]

        for dx, dy in moves:
            ni,nj = i,j
            # Skaczemy do ściany
            while True:
                ti,tj = ni + dx, nj + dy
                if 0 <= ti < n and 0 <= tj < n and D[ti][tj] == "0":
                    ni,nj = ti, tj
                else:
                    break
            #case1
            #Przemieszczenie do (ni,nj) bez próby przebicia
            if dp[ni][nj][przebil] > time + 1:
                dp[ni][nj][przebil] = time + 1
                Q.append((ni,nj,przebil))

            #case2
            #Próba przebicia się
            if przebil == 0:
                ti,tj = ni + 2*dx, nj + 2*dy #pole za ścianą
                mi,mj = ni + dx, nj + dy # ściana, którą chcemy przebić

                if 0 <= ti < n and 0 <= tj < n and 0 <= mi < n and 0 <= mj < n and D[mi][mj] == "#" and D[ti][tj] == "0":
                    if dp[ti][tj][1] > time + 1:
                        dp[ti][tj][1] = time + 1
                        Q.append((ti,tj,1))

    res = min(dp[n-1][n-1][0], dp[n-1][n-1][1])
    return res if res != float("inf") else -1

D = [ "000##",
"##000",
"000##",
"00##0",
"00000" ]
print(kurt(D))




