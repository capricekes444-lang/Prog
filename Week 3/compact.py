
def compact(lst: list[object]) -> list[object]:
    """
    Maakt een nieuwe lijst zonder falsy elementen.
    De originele lijst blijft onveranderd.

    >>> compact([1, 0, 2, 0, 3])
    [1, 2, 3]

    >>> compact(["hello", "", "world", ""])
    ['hello', 'world']

    >>> compact([True, False, 1, 0])
    [True, 1]

    >>> compact([0, "", False, None])
    []

    >>> compact([])
    []

    >>> compact([1, 2, 3])
    [1, 2, 3]

    >>> original = [0, 1, "", 2]
    >>> compact(original)
    [1, 2]
    >>> original
    [0, 1, '', 2]

    >>> compact([[], [1], {}, {"a": 1}])
    [[1], {'a': 1}]
    """
    result = []

    for x in lst:
        if x:
            result.append(x)

    return result
