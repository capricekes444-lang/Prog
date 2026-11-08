
def yell(s: str) -> str:
    """
    Verdubbelt alle uitroeptekens en vraagtekens.

    >>> yell("Hello!")
    'Hello!!'
    >>> yell("How are you?")
    'How are you??'
    >>> yell("Cringe? CRINGE!")
    'Cringe?? CRINGE!!'
    >>> yell("Hello world")
    'Hello world'
    >>> yell("!?")
    '!!??'
    """
    result = ""

    for char in s:
        if char == "!" or char == "?":
            result += char * 2
        else:
            result += char

    return result


if __name__ == "__main__":
    tekst = input()
    print(yell(tekst))
