import random


# Aufgabe 1
def gcd(a, b):
    while True:
        if a < b:  # größere Zahl soll oben stehen
            a, b = b, a
        if b == 0:  # tausche a, b damit 0 % a gilt
            a, b = b, a
        tmp = a % b
        if tmp != 0:
            a, b = b, tmp
        if tmp == 0:  # stopp, wenn gcd = 0 ist
            break
    return b


# Aufgabe 2
def gcd_anz_mod(a, b):
    anz = 0
    while True:
        if a < b:  # größere Zahl soll oben stehen
            a, b = b, a
        if b == 0:  # tausche a, b damit 0 % a gilt
            a, b = b, a
        tmp = a % b
        anz += 1
        if tmp != 0:
            a, b = b, tmp
        if tmp == 0:  # stopp, wenn gcd = 0 ist
            break
    return anz


# Aufgabe 3
def gcd_avg_anz_mod(anz, n):
    counter, summe_anz_modulo = 0, 0
    while counter <= anz:
        a = random.randint(0, n - 1)  # generiere ein zufälliges 0 <= a < n
        b = random.randint(0, n - 1)  # generiere ein zufälliges 0 <= b < n
        if a == 0 and b == 0:
            return 'nicht gültig'
        anz_modulo = gcd_anz_mod(a, b)  # berechne anzahl an Modulo-Berechnungen
        summe_anz_modulo += anz_modulo
        counter += 1
    return summe_anz_modulo / anz


# Aufgabe 5
def erw_euklid(c, d, m):
    g = gcd(c, m)  # Berechne g := gcd(c, m) (Euklidischer Algorithmus)
    if (d % g) != 0:  # Falls g nicht d teilt: keine Lösung - Ende
        return -1
    else:
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
            while y < 0:
                y = y % m
            while y > m:
                y = y % m
            return y
        elif c > m:
            x = d // g * x1  # berechne x~
            while x < 0:
                x = x % m
            while x > m:
                x = x % m
            return x


if __name__ == "__main__":
    print(gcd(282, 240))
    print(gcd(9 ** 100 + 1, 10 ** 100 + 1))
    print()
    print(gcd_anz_mod(9 ** 100 + 1, 10 ** 100 + 1))
    print()
    print(erw_euklid(19, 14, 61))
    print(erw_euklid(6, 3, 15))
    print(erw_euklid(6, 3, 18))
