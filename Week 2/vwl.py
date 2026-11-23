def remove_vowels(s: str) -> str:
    """
    >>> remove_vowels("hello")
    'hll'
    >>> remove_vowels("apple")
    'ppl'
    >>> remove_vowels("AEIOU")
    ''
    >>> remove_vowels("Python")
    'Pythn'
    >>> remove_vowels("just setting up my twitter")
    'jst sttng p my twttr'
    """
    result = ""

    for char in s:
        if char.lower() not in "aeiou":
            result += char

    return result


if __name__ == "__main__":
    tekst = input()
    print(remove_vowels(tekst))