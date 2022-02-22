
# Program wyszukujący w tabeli rezystorów takiej trójki, która posiada łączną rezystancję
# wypadkową równą określonej przez użytkownika wartości

import random

def resistors(tab, n, expected, i=0, r1=0, r2=0, r3=0, counter=0):
    if counter == 3:
        res = 0 #temporary variable to store current resistency
        res += r1
        if res != 0:
            res = (res * r2) / (res + r2)
        else:
            res += r2
        if res != 0:
            res = (res * r3) / (res + r3)
        else:
            res += r3
        res //= 1
        return expected == res
    if i == n:
        return False
    else:
        return resistors(tab, n, expected, i + 1, r1, r2, r3, counter) \
        or resistors(tab, n, expected, i + 1, r1 + tab[i], r2, r3, counter + 1) \
        or resistors(tab, n, expected, i + 1, r1, r2 + tab[i], r3, counter + 1) \
        or resistors(tab, n, expected, i + 1, r1, r2, r3 + tab[i], counter + 1)

if __name__ == '__main__':
    resistency = float(input()) # expected value
    n = int(input()) # size of an array

    tab = [random.randint(0, 100) for i in range(n)] # pseudo-random list

    print(resistors(tab, len(tab), resistency))