import random


def miller_rabin_test(n, it):
    k = n - 1
    while True:
        tmp = it ** k % n
        if tmp != 1 and tmp != (n - 1):
            return 1
        elif tmp == (n - 1) or k % 2 != 0:
            return 0
        k //= 2


def find_Primzahl(n, it):
    if n % 2 == 0:
        n += 1
    while miller_rabin_test(n, it) != 0:
        n += 2
    return n


if __name__ == "__main__":
    print(find_Primzahl(10**100, 10))
