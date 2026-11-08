
def shout(s: str) -> str:
    """
    Zet alle letters om naar hoofdletters.

    >>> shout("hello")
    'HELLO'
    >>> shout("Hello World!")
    'HELLO WORLD!'
    >>> shout("Python")
    'PYTHON'
    >>> shout("abc123")
    'ABC123'
    >>> shout("")
    ''
    """
    result = ""

    for char in s:
        result += char.upper()

    return result


if __name__ == "__main__":
    tekst = input()
    print(shout(tekst))