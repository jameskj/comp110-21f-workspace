"""Exercise number 5."""

__author__ = "730463762"


# This is the first function and will be only_evens.
def only_evens(xs: list[int]) -> list[int]:
    """This function will return all even numbers from a list."""
    ys: list[int] = []
    for x in xs:
        if x % 2 == 0:
            ys.append(x)
    return ys


# This is the second function called sub.
def sub(line: list[int], start: int, end: int) -> list[int]:
    """This function gives a subset of the original function with its parameters."""
    subset: list[int] = []
    if start < 0:
        start = 0
    if start == len(line):
        return subset
    if len(line) == 0:
        return subset
    for x in line:
        if end > len(line):
            if x >= line[start]:
                subset.append(x)
        else:
            if x >= line[start] and x < line[end]:
                subset.append(x)

    return subset


# This is the final function and it puts together two lists.
def concat(list1: list[int], list2: list[int]) -> list[int]:
    """This function puts together list1 and list2."""
    combined: list[int] = []
    for x in list1:
        combined.append(x)
    for x in list2:
        combined.append(x)
    return combined
