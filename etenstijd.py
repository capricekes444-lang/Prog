def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".

    >>> meal("7:15")
    'ontbijt'
    >>> meal("08:00")
    'ontbijt'
    >>> meal("13:00")
    'lunch'
    >>> meal("18:53")
    'avondeten'
    >>> meal("22:12") is None
    True
    """
    uren, minuten = time.split(":")

    uren = int(uren)
    minuten = int(minuten)

    tijd = uren * 60 + minuten

    if 420 <= tijd <= 480:
        return "ontbijt"
    elif 720 <= tijd <= 780:
        return "lunch"
    elif 1080 <= tijd <= 1140:
        return "avondeten"
    else:
        return None


if __name__ == "__main__":
    tijd = input("Hoe laat is het? ")
    resultaat = meal(tijd)

    if resultaat is not None:
        print("Het is tijd voor " + resultaat)