"""Test for only_evens function."""

__author__ = "730463762"

from exercises.ex05.utils import only_evens


def test_only_evens_empty() -> None:
    """Tests the function with an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []
    return None


def test_only_evens_single_odd() -> None:
    """Tests the function with no even integer."""
    xs: list[int] = [3]
    assert only_evens(xs) == []
    return None


def test_only_evens_first_ten() -> None:
    """Tests the function with a full list including even and odd integers."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]
    return None