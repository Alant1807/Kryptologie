import random


def teste_Zeuge(n, a):
    x = pow(a, n - 1, n)
    if x != 1:
        return 1
    k = (n - 1) // 2
    while True:
        x = pow(a, k, n)
        if x != 1 and x != (n - 1):
            return 1
        elif x == (n - 1) or k % 2 != 0:
            return 0
        k //= 2


def miller_rabin_test(n, it):
    for _ in range(it):
        a = random.randint(1, n - 1)
        if teste_Zeuge(n, a):
            return 1
    return 0


def find_Primzahl(n, it):
    if n % 2 == 0:
        n += 1
    while miller_rabin_test(n, it) != 0:
        n += 2
    return n


def anzahl_zeugen(n):
    counter = 0
    for a in range(1, n):
        if teste_Zeuge(n, a) == 1:
            counter += 1
    return counter


def avg_distance_Prim(anz, n, it):
    summe_differenz = 0
    for counter in range(anz + 1):
        m = random.randint(0, n)
        pm = find_Primzahl(m, it)
        differenz = pm - m
        summe_differenz += differenz
    return summe_differenz / anz


if __name__ == "__main__":
    print(find_Primzahl(17, 5))
    print(find_Primzahl(32, 5))
    print(find_Primzahl(10 ** 100, 10))
    print(anzahl_zeugen(9))
    print(anzahl_zeugen(325))
