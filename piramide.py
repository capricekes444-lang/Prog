def print_pyramid(hoogte: int) -> None:
    """
    Print een halve piramide van de gegeven hoogte.
    >>> print_pyramid(5)
    ##
    ###
  ####
 #####
######
    """
    for i in range(1, hoogte + 1):

        for j in range(hoogte - i):
            print(' ', end='')

        for j in range(i + 1):
            print('#', end='')

        print()


if __name__ == '__main__':
    hoogte = int(input("Hoe hoog moet de piramide zijn? "))

    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))
    print_pyramid(hoogte)