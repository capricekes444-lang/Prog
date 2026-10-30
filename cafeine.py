def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
    >>> calculate_cafeine(2, 2, 2, 2)
    510
    >>> calculate_cafeine(3, 5, 1, 2)
    655
    """
    return coffee * 90 + tea * 45 + energy * 80 + cola * 40
if __name__ == '__main__':
    coffee = int(input("Hoeveel koffie heb je gedronken?"))
    tea = int(input("Hoeveel thee heb je gedronken? "))
    energy = int(input("Hoeveel thee heb je gedronken?"))
    result = calculate_cafeine(coffee, tea, energy, cola)
    print(result)