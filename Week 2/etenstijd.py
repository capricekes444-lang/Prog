def meal(time: str) -> str | None:
    """
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
    uur_str, minuut_str = time.split(":")

    uren = int(uur_str)
    minuten = int(minuut_str)

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