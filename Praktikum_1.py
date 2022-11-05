import random


# Aufgabe 1
def gcd(a, b):
    while b != 0:
        tmp = a % b
        a, b = b, tmp
    return a


# Aufgabe 2
def gcd_anz_mod(a, b):
    anz = 0
    while b != 0:
        tmp = a % b
        anz += 1
        a, b = b, tmp
    return anz


# Aufgabe 3
def gcd_avg_anz_mod(anz, n):
    summe_anz_modulo = 0
    for counter in range(anz + 1):
        a = random.randint(0, n - 1)  # generiere ein zufälliges 0 <= a < n
        b = random.randint(0, n - 1)  # generiere ein zufälliges 0 <= b < n
        if a == 0 and b == 0:
            return 'nicht gültig'
        anz_modulo = gcd_anz_mod(a, b)  # berechne anzahl an Modulo-Berechnungen
        summe_anz_modulo += anz_modulo
    return summe_anz_modulo / anz


# Aufgabe 5
def erw_euklid(c, d, m):  # Testziel: lösen von ax + by = gcd(a,b)
    g = gcd(c, m)  # Berechne g := gcd(c, m) (Euklidischer Algorithmus)
    if (d % g) != 0:  # Falls g nicht d teilt: keine Lösung - Ende
        return -1
    rk, xk, yk = 0, 0, 0  # Initilasierung
    r0, r1 = c, m
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    if r0 < r1:  # größere Zahl soll oben stehen
        r0, r1 = r1, r0
    while True:  # Erweiterter euklidischer Algorithmus
        rk = r0 % r1  # berechne rk
        qk = r0 // r1  # berechne qk
        if c < m:
            yk = y0 - (y1 * qk)  # berechne yk
        elif c > m:
            xk = x0 - (x1 * qk)  # berechne xk
        if rk != 0:
            r0, r1 = r1, rk
            if c < m:
                y0, y1 = y1, yk
            elif c > m:
                x0, x1 = x1, xk
        if rk == 0:  # stopp, wenn gcd = 0 ist
            break
    if c < m:
        y = d // g * y1  # berchne y~
        y = y % m
        return y
    elif c > m:
        x = d // g * x1  # berechne x~
        x = x % m
        return x


if __name__ == "__main__":
    # print(gcd(282, 240))
    # print(gcd(9 ** 100 + 1, 10 ** 100 + 1))
    # print()
    # print(gcd_anz_mod(9 ** 100 + 1, 10 ** 100 + 1))
    # print()
    # print(erw_euklid(19, 14, 61))
    # print(erw_euklid(86, 13, 61))
    # print(erw_euklid(6, 3, 15))
    # print(erw_euklid(6, 3, 18))
    # print(erw_euklid(9 ** 100 + 1, 8 ** 100 + 1, 10 ** 100 + 1))
    print(gcd_avg_anz_mod(10000, 10000))
    print(gcd_avg_anz_mod(10000, 100000))
    print(gcd_avg_anz_mod(10000, 1000000))
    print(gcd_avg_anz_mod(10000, 10000000))
    print(gcd_avg_anz_mod(10000, 100000000))
    print(gcd_avg_anz_mod(10000, 1000000000))
# print(gcd_avg_anz_mod(10000, 100000) - gcd_avg_anz_mod(10000, 10000))
# print(gcd_avg_anz_mod(10000,10000000)-gcd_avg_anz_mod(10000,1000000))
# print(gcd_avg_anz_mod(10000,1000000000)-gcd_avg_anz_mod(10000,100000000))
