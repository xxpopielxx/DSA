def maximumGap(nums):
    n = len(nums)
    if n < 2:
        return 0
    low, high = min(nums), max(nums)
    ran = high - low

    buckets = [[] for _ in range(n)]
    for num in nums:
        if num == high:
            ind = n - 1
        else:
            ind = (abs(num - low) * (n - 1)) // ran
        buckets[ind].append(num)

    res_buckets = []
    for i in range(n):
        if buckets[i]:
            res_buckets.append((min(buckets[i]), max(buckets[i])))

    maxi = 0
    for i in range(1, len(res_buckets)):
        maxi = max(maxi, abs(res_buckets[i - 1][-1] - res_buckets[i][0]))
    return maxi

print(maximumGap([3,6,9,1]))