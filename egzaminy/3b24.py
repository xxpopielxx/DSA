
def gen_kunlucky_set(k, max_num):
    kset = set()
    x = k
    i = 1

    while x <= max_num:
        kset.add(x)
        x = x + (x % i) + 7
        i += 1

    return kset


def kunlucky(T, k):
    n = len(T)
    kset = gen_kunlucky_set(k, n)

    i,j = 0,0 # i – początek przedziału, j – koniec przedziału
    cnt, tmp_len, max_len = 0, 0, 0 # licznik, ile k-pechowych mamy w bieżącym oknie, długość aktualnego okna, maksymalna długość

    while j < n:
        if cnt < 3:
            T[j] = T[j] in kset # zamiana liczby na 1 (jeśli k-pechowa) lub 0
            tmp_len += 1
            cnt += T[j]
            j += 1
            if cnt < 3 and max_len < tmp_len:
                max_len = tmp_len

        else:
            tmp_len -= 1 # zmniejszamy długość aktualnego okna
            cnt -= T[i] # jeśli T[i] to 1 (czyli liczba k-pechowa), to zmniejszamy licznik k-pechowych
            i += 1 # przesuwamy początek okna w prawo

    return max_len
