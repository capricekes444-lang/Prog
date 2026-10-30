def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    >>> hoeveelheid_water(minuten: 2)
    24 
    >>> hoeveelheid_water(minuten: 5)
    60
    >>> hoeveelheid_water(minuten: 0)
    0
    """
    return minuten * 10
    
if __name__ == '__main__':
    <vraag input, roep functie aan, en print resultaat