# Aufgabe 1
def gcd(a, b):
    while True:
        if a < b:
            a, b = b, a
        if b == 0:
            a, b = b, a
        tmp = a % b
        if tmp != 0:
            a, b = b, tmp
        if tmp == 0:
            break
    return b


# Aufgabe 2
def gcd_anz_mod(a, b):
    anz = 0
    while True:
        if a < b:
            a, b = b, a
        if b == 0:
            a, b = b, a
        tmp = a % b
        anz += 1
        if tmp != 0:
            a, b = b, tmp
        if tmp == 0:
            break
    return anz


# def gcd_avg_anz_mod(anz, n):


# Aufgabe 5
def erw_euklid(c, d, m):
    g = gcd(c, m)
    if (d % g) != 0:
        return -1
    else:
        rk, xk, yk = 0, 0, 0
        r0, r1 = c, m
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        if r0 < r1:
            r0, r1 = r1, r0
        while True:
            rk = r0 % r1
            qk = r0 // r1
            if c < m:
                yk = y0 - (y1 * qk)
            elif c > m:
                xk = x0 - (x1 * qk)
            if rk != 0:
                r0, r1 = r1, rk
                if c < m:
                    y0, y1 = y1, yk
                elif c > m:
                    x0, x1 = x1, xk
            if rk == 0:
                break
        if c < m:
            y = d // g * y1
            while y > m:
                y = y % m
            return y
        elif c > m:
            x = d // g * x1
            while x > m:
                x = x % m
            return x


if __name__ == "__main__":
    print(erw_euklid(6, 3, 18))
