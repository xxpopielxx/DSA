
T = [2,4,3,6,7]

def kawa(T,k):
    n = len(T)
    dp = [0] * (k+1)
    cnt = 0

    for i in range(n-1,-1,-1):
        for j in range(T[i]):
            cnt += dp[j]
        dp[T[i]] += 1
    return cnt

print(kawa(T,8))