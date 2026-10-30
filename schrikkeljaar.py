def is_leap_year(year: int) -> bool:
    """
    Bepaalt of een jaar een schrikkeljaar is.

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