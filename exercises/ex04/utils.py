"""Using Lists to find duplicates and relative properties."""

__author__ = "730463762"


# This first function will be all
def all(xs: list[int], a: int) -> bool:
    """This function determines if all numbers in a list are equivalent or not."""
    i: int = 0
    if len(xs) < 1:
        return False
    else:
        while i < len(xs):
            item: int = xs[i]
            if item != a:
                return False
            i += 1
        return True


# This second function will be is_equal
def is_equal(ys: list[int], zs: list[int]) -> bool:
    """This function determines if both lists are compiled equally or not."""
    i: int = 0
    if len(ys) == len(zs):
        while i < len(ys):
            item1: int = ys[i]
            item2: int = zs[i]
            if item1 != item2:
                return False
            i += 1
        return True
    else: 
        return False


# This last function will be max
def max(options: list[int]) -> int:
    """This function will return the maximum value in a list."""
    if len(options) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = options[0]
    i: int = 0
    while i < len(options):
        if options[i] > max:
            max = options[i]
        i += 1
                
    return max