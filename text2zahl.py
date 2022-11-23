def wert(a: chr) -> int:
    w = ord(a)

    if w == 0:
        return -1
    if a == 'ä' or a == 'Ä':
        return 96
    if a == 'ö' or a == 'Ö':
        return 97
    if a == 'ü' or a == 'Ü':
        return 98
    if a == 'ß':
        return 99

    w -= 32
    if w < 0 or w > 99:
        return 0

    return w


def buch(w: int) -> chr:
    if w == 96:
        return 'ä'
    if w == 97:
        return 'ö'
    if w == 98:
        return 'ü'
    if w == 99:
        return 'ß'
    return chr(w + 32)


def text2zahl(text: str) -> int:
    basis = 1
    zahl = 0
    for i in range(len(text) - 1, -1, -1):
        zahl += basis * wert(text[i])
        basis *= 100
    return zahl


def zahl2text(zahl: int) -> str:
    text = []
    while zahl > 0:
        wert = zahl % 100
        text.append(buch(wert))
        zahl = zahl // 100
    return "".join(text[::-1])


if __name__ == "__main__":
    txt = "Deutschland hat seinen Start in die WM 2022 verpatzt und mit 1:2 gegen Japan verloren."
    print(text2zahl(txt))
