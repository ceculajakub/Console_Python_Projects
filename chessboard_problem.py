# Król szachowy przechodzi po szachownicy 8x8 wypełnionej liczbami naturalnymi.
# Jego zadaniem jest dostanie się do prawego dolnego narożnika.
# Może poruszyć się na sąsiednie pole, tylko wtedy gdy ten ruch nie oddala go od celu
# oraz ostatnia cyfra liczba przypisanej do pola, na którym stoi jest mniejsza od
# pierwszej cyfy liczby przypisanej do pola docelowego.
# Funkcja ta sprawdza czy dla podanej szachownicy istnieje taka droga.


def first_number(n):
    while n > 9:
        n //= 10
    return n


# r - row, c - column , pos - last position
def path_check(tab, r, c, pos):
    if r < 0 or r >= 8 or c < 0 or c >= 8:
        return False

    if r != 0 or c != 0:
        if pos < 10:
            if first_number( tab[r][c] ) > pos:
                return True
            else:
                return False
        else:
            if first_number( tab[r][c] ) > pos % 10:
                return True
            else:
                return False

    if r == 7 and c == 7:
        return True
    pos = tab[r][c]
    paths = [None] * 3


    paths[0] = path_check(tab, r + 1, c, pos)
    paths[1] = path_check(tab, r + 1, c + 1, pos)
    paths[2] = path_check(tab, r, c + 1, pos)

    for i in range(3):
        if paths[i]:
            return True

    return False


if __name__ == '__main__':

    # example of a list which meets the conditions
    tab = [
        [1, 4, 6, 2, 3, 5, 35, 2],
        [1, 4, 6, 2, 3, 5, 35, 2],
        [1, 4, 6, 82, 3, 5, 35, 2],
        [1, 4, 6, 2, 3, 5, 35, 2],
        [1, 4, 6, 2, 3, 5, 91, 2],
        [1, 4, 6, 82, 3, 5, 24, 2],
        [1, 4, 6, 2, 3, 5, 35, 7],
        [1, 4, 6, 2, 3, 5, 35, 8],
    ]


    print(path_check(tab, 0, 0, tab[0][0]))
