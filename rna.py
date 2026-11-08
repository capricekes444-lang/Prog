
def check_input(dna: str) -> bool:
    """
    Controleert of de DNA-string geldig is.

    >>> check_input("ATGC")
    True
    >>> check_input("atGcA")
    True
    >>> check_input("hello")
    False
    >>> check_input("ATGX")
    False
    >>> check_input("ATCG")
    True
    """
    if dna == "":
        return False

    for char in dna:
        if char.upper() not in "AGCT":
            return False

    return True


def transcribe_dna_to_rna(dna: str) -> str:
    """
    Zet DNA om naar RNA in hoofdletters.

    >>> transcribe_dna_to_rna("ATGC")
    'UACG'
    >>> transcribe_dna_to_rna("atGcAgtAttGCA")
    'UACGUCAUAACGU'
    >>> transcribe_dna_to_rna("CTGAC")
    'GACUG'
    """
    result = ""

    for char in dna.upper():
        if char == "A":
            result += "U"
        elif char == "G":
            result += "C"
        elif char == "C":
            result += "G"
        elif char == "T":
            result += "A"

    return result


if __name__ == "__main__":
    dna = input("DNA: ")

    if check_input(dna):
        rna = transcribe_dna_to_rna(dna)
        print("RNA:", rna)
    else:
        print("That is not a valid DNA string")