def is_leap_year(year: int) -> bool:
    """
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2025)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
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

    if is_leap_year(year):
        print(f"{year} is een schrikkeljaar")
    else:
        print(f"{year} is geen schrikkeljaar")