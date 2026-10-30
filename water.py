def hoeveelheid_water(minuten: int) -> int:
    """
    Geeft de hoeveelheid water uit de douche, gerekend in flesjes,
    gegeven het aantal minuten douchen.
    >>> hoeveelheid_water(2)
    24 
    >>> hoeveelheid_water(5)
    60
    >>> hoeveelheid_water(0)
    0
    """
    return minuten * 12
    
if __name__ == '__main__':
    minuten = int(input("Hoeveel minuten douche je?"))
    result = hoeveelheid_water(minuten)
    print(result)