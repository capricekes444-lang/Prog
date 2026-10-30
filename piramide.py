def print_pyramid(hoogte: int) -> None:
    """
    Print een halve piramide van de gegeven hoogte.

    >>> print_pyramid(3)
      ##
     ###
    ####
    """
    for i in range(1, hoogte + 1):
        for j in range(hoogte - i):
            print(' ', end='')

        for j in range(i + 1):
            print('#', end='')

        print()