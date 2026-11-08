
def calculate_grade(text: str) -> int:
    """
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    -9
    >>> calculate_grade("Hello world.")
    -1
    >>> calculate_grade("Hello.")
    -16
    >>> calculate_grade("Hi.")
    -34
    """
    letters = 0
    words = 0
    sentences = 0
    in_word = False

    for char in text:
        if char.isalpha():
            letters += 1

        if char.isalnum():
            if not in_word:
                words += 1
                in_word = True
        else:
            in_word = False

        if char in ".!?":
            sentences += 1

    return coleman_liau(words, sentences, letters)


def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de Coleman-Liau-index.

    >>> coleman_liau(8, 4, 29)
    -9
    >>> coleman_liau(10, 2, 50)
    8
    >>> coleman_liau(5, 1, 20)
    2
    >>> coleman_liau(0, 0, 0)
    0
    """
    if words == 0:
        return 0

    L = letters / words * 100
    S = sentences / words * 100

    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)


if __name__ == "__main__":
    text = input("Text: ")
    grade = calculate_grade(text)

    if grade < 1:
        print("Below Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print("Grade", grade)