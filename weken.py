def weeks_elapsed(day1: int, day2: int) -> int:
    """
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return abs(day2 - day1) // 7