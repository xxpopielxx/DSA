
def kintersect(A, k):
    intervals = []
    i = 0
    while i < len(A):
        intervals.append((A[i][0],A[i][1], i))
        i += 1

    intervals.sort(key=lambda x: x[0])

    max_length = -1
    res = []

    i = 0
    while i + k <= len(intervals):
        window = intervals[i:i+k]

        max_start = window[-1][0]
        min_end = window[0][1]
        j = 1
        while j < k:
            if window[j][1] < min_end:
                min_end = window[j][1]
            j += 1

        length = min_end - max_start
        if length > max_length:
            max_length = length
            res = []
            j = 0
            while j < k:
                res.append(window[j][2])
                j += 1
        i += 1

    return res




A = [(0,4),(1,10),(6,7), (2,8)]
print(kintersect(A,3))



