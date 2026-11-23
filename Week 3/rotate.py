
def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]

    >>> n2 = [1, 2, 3, 4, 5]
    >>> rotate(n2)
    >>> n2
    [2, 3, 4, 5, 1]

    >>> n3 = [7]
    >>> rotate(n3)
    >>> n3
    [7]

    >>> n4 = ["a", "b", "c"]
    >>> rotate(n4)
    >>> n4
    ['b', 'c', 'a']

    >>> n5 = [1, 1, 2, 2]
    >>> rotate(n5)
    >>> n5
    [1, 2, 2, 1]
    """
    if len(lst) <= 1:
        return

    first = lst[0]

    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]

    lst[-1] = first
