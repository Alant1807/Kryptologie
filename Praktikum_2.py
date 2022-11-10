import random


def miller_rabin_test(n, it):
    k = n - 1
    while True:
        tmp = pow(it, k, n)
        if tmp != 1 and tmp != (n - 1):
            return 1
        elif tmp == (n - 1) or (k % 2 != 0 and tmp == 1 or tmp == (n - 1)):
            return 0
        k //= 2


def find_Primzahl(n, it):
    if n % 2 == 0:
        n += 1
    while miller_rabin_test(n, it) != 0:
        n += 2
    return n


def anzahl_zeugen(n):
    counter = 0
    for it in range(1, n):
        if miller_rabin_test(n, it) == 1:
            counter += 1
    return counter


def avg_distance_Prim(anz, n, it):
    summe_differenz = 0
    for counter in range(anz + 1):
        m = random.randint(1, n - 1)
        pm = find_Primzahl(m, it)
        differenz = pm - m
        summe_differenz += differenz
    return summe_differenz / anz


if __name__ == "__main__":
    print(avg_distance_Prim(1000, 1))
