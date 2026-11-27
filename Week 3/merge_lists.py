def merge_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    >>> merge_lists([1, 3], [2, 4, 6])
    [1, 2, 3, 4, 6]
    >>> merge_lists([], [1, 2])
    [1, 2]
    >>> merge_lists([1, 2], [])
    [1, 2]
    >>> merge_lists([], [])
    []
    """
    result = []
    i = 0
    j = 0 
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    if i < len(lst1):
        for k in range(i, len(lst1)):
            result.append(lst1[k])
    else:
        for k in range(j, len(lst2)):
            result.append(lst2[k])

    return result