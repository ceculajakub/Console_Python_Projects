# Funkcja wypełniająca tablicę dwuwymiarową kolejnymi liczbami nautralnymi przy użyciu schematu spirali.

def spiral(tab,n): # n - array size

    Top = 0
    Bottom = n-1
    Left = 0
    Right = n-1
    number = 0
    direction = 0 # variable which indicates change of direction
    # 0 - going towards right border
    # 1 - going towards bottom border
    # 2 - going towards left border
    # 3 - going towards top border

    while(Top <= Bottom) and (Left <= Right):

        if direction == 0:

            for i in range(Left, Right + 1):

                tab[Top][i] = number

                print(tab[Top][i])

                number += 1

            Top += 1

            direction += 1

        elif direction == 1:

            for i in range(Top, Bottom + 1):

                tab[i][Right] = number

                print(tab[i][Right])

                number += 1

            Right -= 1

            direction += 1

        elif direction == 2:

            for i in range(Right, Left - 1, -1):

                tab[Bottom][i] = number

                print(tab[Bottom][i])

                number += 1

            Bottom -= 1

            direction += 1

        elif direction == 3:

            for i in range(Bottom, Top - 1, -1):

                tab[i][Left] = number

                print(tab[i][Left])

                number += 1

            Left += 1

            direction = 0

if __name__ == '__main__':

    n = int(input("Please enter demanded size of an array: "))

    tab = [None] * n

    for i in range(n):

        tab[i] = [None] * n

    spiral(tab,n)

