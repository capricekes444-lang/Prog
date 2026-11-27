POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


def compute_score(word: str) -> int:
    """
    Bereken de score van een woord door de punten
    van alle letters bij elkaar op te tellen.

    >>> compute_score("code")
    7
    >>> compute_score("CODE")
    7
    >>> compute_score("Hallo!")
    8
    >>> compute_score("")
    0
    >>> compute_score("123!")
    0
    """
    score = 0

    for letter in word:
        score += compute_letter_score(letter)

    return score


def compute_letter_score(letter: str) -> int:
    """
    Zoek met een loop de positie van de letter in het
    alfabet en return de bijbehorende waarde uit POINTS.
    Tekens die niet in het alfabet staan krijgen 0 punten.

    >>> compute_letter_score("a")
    1
    >>> compute_letter_score("B")
    3
    >>> compute_letter_score("z")
    10
    >>> compute_letter_score("!")
    0
    >>> compute_letter_score("5")
    0
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()

    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            return POINTS[i]

    return 0


if __name__ == '__main__':
    word1 = input("Speler 1: ")
    word2 = input("Speler 2: ")

    score1 = compute_score(word1)
    score2 = compute_score(word2)

    if score1 > score2:
        print("Speler 1 wint!") 
    elif score2 > score1:
        print("Speler 2 wint!")
    else:
        print("Gelijkspel!")