"""Practicing Function Definitions."""

__author__ = "730463762"


def my_max(a: int, b: int) -> int:
    if a >= b: 
        return a
    else:
        return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)