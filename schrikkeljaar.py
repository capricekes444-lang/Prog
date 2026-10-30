def is_schrikkel(year: int) -> bool:
    """
    Controleert of een jaar een schrikkeljaar is.

    >>> is_schrikkel(2024)
    True
    >>> is_schrikkel(2025)
    False
    >>> is_schrikkel(1900)
    False
    >>> is_schrikkel(2000)
    True
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    year = int(input("Geef een jaartal: "))

    if is_schrikkel(year):
        print(f"{year} is een schrikkeljaar")
    else:
        print(f"{year} is geen schrikkeljaar")