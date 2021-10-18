"""Sum function."""

__author__ = "730463762"


def sum(xs: list[float]) -> float:
    """We are finding the sum of numbers."""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total