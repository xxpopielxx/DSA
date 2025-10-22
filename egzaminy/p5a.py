#0(n^2)
def inwestor(T):
    n = len(T)
    max_sum = 0
    for i in range(n):
        mini = T[i]
        for j in range(i,n):
            mini = min(mini, T[j])
            ln = j - i + 1
            max_sum = max(max_sum,  ln * mini)

    return max_sum


#0(n)
def inwestor1(T):
    n = len(T)
    stack = []
    max_area = 0
    T.append(0)

    for i in range(len(T)):
        while stack and T[i] < T[stack[-1]]:
            h = T[stack.pop()]
            width = i if not stack else i - (stack[-1] + 1)
            max_area = max(max_area, h * width)
        stack.append(i)
    return max_area



