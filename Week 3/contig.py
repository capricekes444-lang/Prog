
def contig(lst: list[int]) -> list[list[int]]:
    """
    Verdeelt een lijst in groepen van opeenvolgende integers.

    >>> contig([1, 2, 3, 5, 6, 9])
    [[1, 2, 3], [5, 6], [9]]

    >>> contig([1, 2, 3, 4])
    [[1, 2, 3, 4]]

    >>> contig([1, 3, 5, 7])
    [[1], [3], [5], [7]]

    >>> contig([])
    []

    >>> contig([5])
    [[5]]

    >>> contig([1, 2, 2, 3, 4])
    [[1, 2], [2, 3, 4]]

    >>> contig([5, 4, 3, 2])
    [[5], [4], [3], [2]]

    >>> contig([-3, -2, -1, 2, 3])
    [[-3, -2, -1], [2, 3]]

    >>> original = [1, 2, 5]
    >>> contig(original)
    [[1, 2], [5]]
    >>> original
    [1, 2, 5]
    """
    result = []

    if len(lst) == 0:
        return result

    part = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            part.append(lst[i])
        else:
            result.append(part)
            part = [lst[i]]

    result.append(part)

    return result
