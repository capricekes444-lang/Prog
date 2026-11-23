
def uniq(lst: list[object]) -> list[object]:
    """
    >>> uniq([1, 2, 2, 3, 1])
    [1, 2, 3]

    >>> uniq([1, 1, 1, 1])
    [1]

    >>> uniq([])
    []

    >>> uniq([1, 2, 3])
    [1, 2, 3]

    >>> uniq(["a", "b", "a", "c", "b"])
    ['a', 'b', 'c']

    >>> uniq([0, 0, False, 1, True])
    [0, 1]

    >>> uniq([5])
    [5]

    >>> original = [1, 2, 2, 3]
    >>> uniq(original)
    [1, 2, 3]
    >>> original
    [1, 2, 2, 3]
    """
    result = []

    for i in range(len(lst)):
        if lst[i] not in result:
            result.append(lst[i])

    return result
