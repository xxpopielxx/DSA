
def counting(T):
    M = max(T)
    count_array = [0] * (M + 1)

    for num in T:
        count_array[num] += 1

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(T)

    for i in range(len(T) - 1, -1, -1):
        output_array[count_array[T[i]] - 1] = T[i]
        count_array[T[i]] -= 1

    return output_array


T = [2,5,3]
print(counting(T))