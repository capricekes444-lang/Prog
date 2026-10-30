def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten.
    >>> travel_costs(4)
    0.52
    >>> travel_costs(1)
    0.13
    >>> travel_costs(10)
    1.3
    """
    return round(km * 0.13, 2)

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
    Bepaalt de totale kosten.

    >>> total_costs(2, 2)
    120
    >>> total_costs(1, 1)
    60
    >>> total_costs(2, 3)
    180
    """
    return round(travel_costs(km) + overnight_costs(nights))

if __name__ == '__main__':
    km = int(input("Hoeveel kilometers heb je gereisd? "))
    nights = int(input("Hoeveel nachten ben je gebleven? "))

    results = total_costs(km, nights)
    print(results)