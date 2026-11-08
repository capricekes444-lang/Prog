def get_positive_int() -> int:
    """
    Vraagt om een positief geheel getal.
    """
    result = int(input("Enter a positive int: "))

    while result <= 0:
        result = int(input("Enter a positive int: "))

    return result


def get_any_int_but_0() -> int:
    """
    Vraagt om een geheel getal behalve 0.
    """
    result = int(input("Enter an int except 0: "))

    while result == 0:
        result = int(input("Enter an int except 0: "))

    return result


def get_min_int(minimum: int) -> int:
    """
    Vraagt om een geheel getal dat minimaal minimum is.
    """
    result = int(input("Enter an int: "))

    while result < minimum:
        result = int(input("Enter an int: "))

    return result


def get_two_different_ints() -> tuple[int, int]:
    """
    Vraagt om twee verschillende gehele getallen.
    """
    first = int(input("Enter first int: "))
    second = int(input("Enter second int: "))

    while first == second:
        first = int(input("Enter first int: "))
        second = int(input("Enter second int: "))

    return first, second

if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()