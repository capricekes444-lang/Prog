def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten voor heen en terug.

    >>> travel_costs(4)
    1.04
    >>> travel_costs(1)
    0.26
    >>> travel_costs(10)
    2.6
    """
    return km * 2 * 0.13


def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten.

    >>> overnight_costs(1)
    60
    >>> overnight_costs(2)
    120
    >>> overnight_costs(10)
    600
    """
    return nights * 60


def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale vakantiekosten.

    >>> total_costs(2, 2)
    121
    >>> total_costs(1, 1)
    60
    >>> total_costs(2, 3)
    181
    """
    costs = travel_costs(km) + overnight_costs(nights)
    return int(costs + 0.5)

if __name__ == '__main__':
    km = int(input("Hoeveel kilometers heb je gereisd? "))
    nights = int(input("Hoeveel nachten ben je gebleven? "))

    results = total_costs(km, nights)
    print(f"Jouw vakantie kost: {results}")