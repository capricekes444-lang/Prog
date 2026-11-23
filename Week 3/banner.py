
def longest_word_from_list(lst: list[str]) -> str:
    """
    >>> longest_word_from_list(["kat", "hond", "olifant"])
    'olifant'
    >>> longest_word_from_list(["appel", "peer", "banaan"])
    'banaan'
    >>> longest_word_from_list(["a", "bb", "ccc"])
    'ccc'
    >>> longest_word_from_list(["hallo"])
    'hallo'
    """
    longest = ""

    for word in lst:
        if len(word) > len(longest):
            longest = word

    return longest


def print_banner(lst: list[str]) -> None:
    """
    Print een banner met hekjes.

    >>> print_banner(["Margherita", "Tutta", "la", "Vita"])
    ##########
    Margherita
    Tutta
    la
    Vita
    ##########

    >>> print_banner(["Hallo", "wereld"])
    ######
    Hallo
    wereld
    ######

    >>> print_banner(["Python"])
    ######
    Python
    ######

    >>> print_banner([])
    """
    longest = longest_word_from_list(lst)

    if len(lst) == 0:
        return

    border = "#" * len(longest)

    print(border)

    for word in lst:
        print(word)

    print(border)


def string_to_list(s: str) -> list[str]:
    """
    Zet een string om in een lijst met woorden.

    >>> string_to_list("Hallo wereld")
    ['Hallo', 'wereld']

    >>> string_to_list("Margherita Tutta la Vita")
    ['Margherita', 'Tutta', 'la', 'Vita']

    >>> string_to_list("Python")
    ['Python']

    >>> string_to_list("")
    []

    >>> string_to_list("een twee drie")
    ['een', 'twee', 'drie']
    """
    result = []
    word = ""

    for letter in s:
        if letter == " ":
            result.append(word)
            word = ""
        else:
            word += letter

    if word != "":
        result.append(word)

    return result


def main() -> None:
    message = input("Typ je boodschap: ")
    words = string_to_list(message)
    print_banner(words)


if __name__ == "__main__":
    main()
