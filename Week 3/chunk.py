
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

    >>> original = [1, 2, 3, 4]
    >>> chunk(original, 2)
    [[1, 2], [3, 4]]
    >>> original
    [1, 2, 3, 4]
    """
    if n <= 0:
        raise ValueError("n moet groter zijn dan 0")

    result = []

    for i in range(0, len(lst), n):
        part = lst[i:i + n]
        result.append(part)

    return result
