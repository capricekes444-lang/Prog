def check_answer(answer: str) -> bool:
    """
    >>> check_answer("tweeenveertig")
    True
    >>> check_answer("tweeënveertig")
    True
    >>> check_answer("42") 
    True
    >>> check_answer("43")
    False
    """
   
    if answer == "42" or answer == "tweeenveertig" or answer == "tweeënveertig":
        return True 
    else:
        return False
if __name__ == '__main__':
    answer = input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?")

    if check_answer(answer):
        print("Ja")
    else:
        print("Nee")