
def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.

    >>> check_length("Hallo123")
    True
    >>> check_length("hoi")
    False
    """
    return len(password) >= 8


def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord een hoofdletter en kleine letter bevat.

    >>> check_letter("Hallo")
    True
    >>> check_letter("hallo")
    False
    """
    hoofdletter = False
    kleine_letter = False

    for teken in password:
        if teken.isupper():
            hoofdletter = True
        if teken.islower():
            kleine_letter = True

    return hoofdletter and kleine_letter


def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.

    >>> check_number("Hallo123")
    True
    >>> check_number("Hallo")
    False
    """
    for teken in password:
        if teken.isdigit():
            return True

    return False


def check_password(password: str) -> bool:
    """
    Controleer of aan alle drie de eisen is voldaan.

    >>> check_password("AardappelTester123")
    True
    >>> check_password("hoi")
    False
    """
    return (check_length(password)
            and check_letter(password)
            and check_number(password))


if __name__ == "__main__":
    password = input("Geef een wachtwoord: ")

    if check_password(password):
        print("Het gegeven wachtwoord is valide.")
    else:
        print("Het gegeven wachtwoord is niet valide.")
