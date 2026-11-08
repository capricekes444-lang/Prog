def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.

    >>> evaluate(1, "+", 1)
    2.0
    >>> evaluate(100, "-", 9)
    91.0
    >>> evaluate(4, "*", -6)
    -24.0
    >>> evaluate(3, "/", 8)
    0.375
    >>> evaluate(-5, "+", 2)
    -3.0
    """
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    else:
        return float(x / z)


if __name__ == "__main__":
    formule = input()
    x_str, y, z_str = formule.split()

    x = int(x_str)
    z = int(z_str)

    resultaat = evaluate(x, y, z)
    print(resultaat)