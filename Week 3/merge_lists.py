def merge_lists(lst1: list[int], lst2: list[int]) -> list[int]:
2, 4, 5, 5, 6]
    >>> merge_lists([1, 3], [2, 4, 6])
    [1, 2, 3, 4, 6]
    >>> merge_lists([], [1, 2])
    [1, 2]
    >>> merge_lists([1, 2], [])
    [1, 2]
    >>> merge_lists([], [])
    []
    result = []
    i = 0
    j = 0 