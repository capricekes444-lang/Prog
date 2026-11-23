
def interleave(lst1: list[object], lst2: list[object], keep: bool) -> list[object]:
    """
    Voegt elementen van twee lijsten afwisselend samen.

    >>> interleave([1, 2, 3], [4, 5, 6], True)
    [1, 4, 2, 5, 3, 6]

    >>> interleave([1, 2, 3], [4, 5, 6], False)
    [1, 4, 2, 5, 3, 6]

    >>> interleave([1, 2, 3, 4], [5, 6], True)
    [1, 5, 2, 6, 3, 4]

    >>> interleave([1, 2, 3, 4], [5, 6], False)
    [1, 5, 2, 6]

    >>> interleave([1], [2, 3, 4], True)
    [1, 2, 3, 4]

    >>> interleave([1], [2, 3, 4], False)
    [1, 2]

    >>> interleave([], [1, 2], True)
    [1, 2]

    >>> interleave([], [1, 2], False)
    []

    >>> interleave([], [], True)
    []

    >>> a = [1, 2, 3]
    >>> b = [4, 5]
    >>> interleave(a, b, True)
    [1, 4, 2, 5, 3]
    >>> a
    [1, 2, 3]
    >>> b
    [4, 5]
    """
    result = []

    for i in range(min(len(lst1), len(lst2))):
        result.append(lst1[i])
        result.append(lst2[i])

    if keep:
        for i in range(min(len(lst1), len(lst2)), len(lst1)):
            result.append(lst1[i])

        for i in range(min(len(lst1), len(lst2)), len(lst2)):
            result.append(lst2[i])

    return result
