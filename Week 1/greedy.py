def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten van 25, 10, 5 en 1 cent.

    >>> count_coins(41)
    4
    >>> count_coins(25)
    1
    >>> count_coins(0)
    0
    >>> count_coins(99)
    9
    """
    count = 0

    while cents >= 25:
        cents = cents - 25
        count = count + 1

    while cents >= 10:
        cents = cents - 10
        count = count + 1

    while cents >= 5:
        cents = cents - 5
        count = count + 1

    while cents >= 1:
        cents = cents - 1
        count = count + 1

    return count


if __name__ == '__main__':
    amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))

    while amount < 0:
        amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))

    cents = round(amount * 100)
    result = count_coins(cents)
    print(result)