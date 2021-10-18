"""Test for invert function."""

__author__ = "730463762"

from exercises.ex06.dictionaries import count


def test_count_empty() -> None:
    """Testing the count function with an empty list."""
    scroll: list[str] = []
    assert count(scroll) == {}
    return None


def test_count_multiple_values() -> None:
    """Testing the count function to see what occured when there are multiple values in the created dictionary."""
    scroll: list[str] = ["pie", "cake"]
    assert count(scroll) == {"pie": 1, "cake": 1}
    return None


def test_count_standard_list() -> None:
    """Testing the count function with a singular mode in the data."""
    scroll: list[str] = ["pie", "pie", "pie", "pizza", "pizza", "cake"]
    assert count(scroll) == {"pie": 3, "pizza": 2, "cake": 1}
    return None