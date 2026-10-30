def print_pyramid(hoogte: int) -> None:
    """
  >>> print_pyramid(1)
    ##
    >>> print_pyramid(2)
     ##
    ###
    >>> print_pyramid(3)
      ##
     ###
    ####
    >>> print_pyramid(4)
       ##
      ###
     ####
    #####
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