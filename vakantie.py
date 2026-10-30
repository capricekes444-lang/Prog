def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accomodatie (tel `km` twee keer voor heen en terug).
    >>> travel_costs(4)
    0.62
    >>> travel_costs(1)
    0.13
    >>> travel_costs(10)
    1.30
    """

def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten op basis van het aantal nachten
    dat je op vakantie gaat.
    >>> overnight_costs(1)
    60
    >>> overnight_costs(2)
    120
    >>> overnight_costs(10)
    600
    """

def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.
    Deze functie delegeert zoveel mogelijk werk naar de andere
    twee functies (roep die dus hier aan).
    >>> total_costs(2, 2)
    121
    >>> total_costs(1, 1)
    60
    >>> total_costs(2, 3) 
    181
    """

if __name__ == '__main__':
    int(input("Hoeveel km heb je gerezen?"))
    <Schrijf hier code die input van de gebruiker opvraagt,
    total_costs aanroept, en print hoeveel de vakantie gaat kosten>