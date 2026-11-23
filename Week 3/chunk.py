
def chunk(lst: list[int], n: int) -> list[list[int]]:
    """
    >>> chunk([1, 2, 3, 4, 5, 6], 2)
    [[1, 2], [3, 4], [5, 6]]

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]

    >>> chunk([1, 2, 3, 4, 5, 6], 3)
    [[1, 2, 3], [4, 5, 6]]

    >>> chunk([1, 2, 3], 1)
    [[1], [2], [3]]

    >>> chunk([1, 2, 3], 5)
    [[1, 2, 3]]

    >>> chunk([], 2)
    []
    """
    result = []
    part = []

    for i in range(len(lst)):
        part.append(lst[i])

        if len(part) == n:
            result.append(part)
            part = []

    if part:
        result.append(part)

    return result
