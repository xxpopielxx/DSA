
def trip(M):
    m, n = len(M), len(M[0])

    dp = [[-1 for _ in range(n)] for _ in range(m)]

    moves =[(-1,0),(1,0),(0,-1),(0,1)]

    def dfs(i,j):
        if dp[i][j] != -1:
            return dp[i][j]

        maxi = 1
        for di,dj in moves:
            ni, nj = di + i, dj + j
            if 0 <= ni < m and 0 <= nj <= n and dp[ni][nj] > dp[i][j]:
                maxi = max(maxi, dfs(ni,nj))

        dp[i][j] = maxi
        return dp[i][j]

    return max(dfs(i,j) for i in range(m) for j in range(n))











