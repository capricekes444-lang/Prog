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
    if __name__ == '__main__':
    day1 = int(input("Dagnummer 1: int"))
    day2 = int(input("Dagnummer 2: "))
    result = ...
    print(f"Er zijn {result} volle weken verstreken.")