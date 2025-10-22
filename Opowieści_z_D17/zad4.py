
#n^2
def wyprawy(WI):
    n = len(WI)
    maxi = 0
    for i in range(n):
        a,b,value = WI[i]
        current = value
        for j in range(i+1, n):
            aj,bj,value_j = WI[j]
            if aj >= b or a >= bj: #nie przcinają się w sensie mogą się konczyc i zaczynać w tym samym momencie
                current += value_j
        maxi = max(maxi, current)

    return maxi

#nlogn z binary searchem, nie działa xd
def wyprawy1(WI):
    WI.sort(key=lambda x: x[1])

    ends = [w[1] for w in WI]

    dp = [0] * len(WI)

    def binary(i):
        left = 0
        right = i-1
        res = -1
        while left <= right:
            mid = (left + right)//2
            if ends[mid] < WI[i][0]:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

    for i in range(len(WI)):
        s,t,k = WI[i]
        j = binary(i)
        if j != -1:
            dp[i] = max(dp[i-1], dp[j] + k)
        else:
            dp[i] = max(dp[i-1], k)

    return dp[-1] if dp else 0


# Przykład 1 (podany w zadaniu)
WI1 = [(1, 5, 100), (3, 4, 70), (2, 4, 90), (4, 7, 60)]
# Oczekiwany wynik: 160 (wyprawy (2,4,90) i (4,7,60))

# Przykład 2
WI2 = [(1, 2, 50), (2, 3, 60), (3, 4, 70), (4, 5, 80)]
# Wszystkie wyprawy nie nachodzą – można zrobić wszystkie
# Wynik: 50 + 60 + 70 + 80 = 260

# Przykład 3
WI3 = [(1, 3, 100), (2, 4, 200), (3, 5, 150)]
# Najlepiej wybrać wyprawę (2,4,200)
# Wynik: 250

# Przykład 4
WI4 = [(1, 10, 100), (2, 3, 50), (4, 5, 50), (6, 7, 50), (8, 9, 50)]
# Lepiej wziąć krótsze wyprawy 4x50 niż jedną długą 100
# Wynik: 200

# Przykład 5
WI5 = [(1, 2, 10), (1, 2, 100), (3, 4, 100), (5, 6, 100)]
# Pierwsze dwa się pokrywają – wybieramy lepsze
# Wynik: 100 + 100 + 100 = 300


print(wyprawy(WI1))
print(wyprawy(WI2))
print(wyprawy(WI3))
print(wyprawy(WI4))
print(wyprawy(WI5))

print(wyprawy1(WI1))
print(wyprawy1(WI2))
print(wyprawy1(WI3))
print(wyprawy1(WI4))
print(wyprawy1(WI5))
