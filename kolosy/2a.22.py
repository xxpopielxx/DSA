
def drivers(P, B):
    P.sort()

    switch_points = []
    for i in range(len(P)):
        if P[i][1]:
            switch_points.append(P[i][0])

    switch_points = [0] + switch_points + [B]
    k = len(switch_points)

    control_cnt = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, min(i+4,k)):
            cnt = 0
            start = switch_points[i]
            end = switch_points[j]
            for t in range(len(P)):
                if not P[t][1]:
                    if start < P[t][0] <= end:
                        cnt += 1
            control_cnt[i][j] = cnt


    dp = [[float("inf"), float("inf")] for _ in range(k)]
    prev = [[-1, -1] for _ in range(k)]

    dp[0][0] = 0
    # DP: dp[i][p] = minimum control points passed by Marian ending at switch i,
    # p=0 if Jacek, p=1 if Marian

    for i in range(k):
        for j in range(i+1, min(i+4,k)):
            if dp[i][0] + control_cnt[i][j] < dp[j][1]:
                dp[j][1] = dp[i][0] + control_cnt[i][j]
                prev[j][1] = i

            if dp[i][1] < dp[j][0]:
                dp[j][0] = dp[i][1]
                prev[j][0] = i


    current = k-1
    driver = 0 if dp[current][0] <= dp[current][1] else 1

    path = []
    while current != 0:
        previous = prev[current][driver]
        if previous != 0 and previous != -1:
            path.append(switch_points[previous])
        driver = 1 - driver
        current = previous
    path.reverse()

    return path


#źle raczej