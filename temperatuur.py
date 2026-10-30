def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet Celsius om naar Fahrenheit of andersom.

    >>> convert_temperature("C", 0)
    32
    >>> convert_temperature("C", 20)
    68
    >>> convert_temperature("F", 32)
    0
    >>> convert_temperature("F", 100)
    37
    """
    if old_type.upper() == "C":
        return int((18 * old_temp + 320) / 10)
    else:
        return int((10 * old_temp - 320) / 18)


def print_table(old_type: str, begin_temp: int,
                end_temp: int, step_size: int) -> None:
    """
    Print een conversietabel.

    >>> print_table("C", 0, 10, 5)
      C |   F
      0 |  32
      5 |  41
     10 |  50

    >>> print_table("F", 10, 0, 2)
      F |   C

    >>> print_table("F", 0, 3, 3)
      F |   C
      0 | -17
      3 | -16
    """
    old_type = old_type.upper()

    if old_type == "C":
        new_type = "F"
    else:
        new_type = "C"

    print(f"{old_type:>3} | {new_type:>3}")

    for temp in range(begin_temp, end_temp + 1, step_size):
        converted = convert_temperature(old_type, temp)
        print(f"{temp:>3} | {converted:>3}")


if __name__ == '__main__':
    old_type = input("Welke eenheid van temperatuur (C of F)? ")

    while old_type.upper() != "C" and old_type.upper() != "F":
        old_type = input("Welke eenheid van temperatuur (C of F)? ")

    begin_temp = int(input("Wat is de begintemperatuur? "))
    end_temp = int(input("Wat is de eindtemperatuur? "))

    step_size = int(input("Wat is de stapgrootte? "))

    while step_size <= 0:
        step_size = int(input("Wat is de stapgrootte? "))

    print_table(old_type, begin_temp, end_temp, step_size)