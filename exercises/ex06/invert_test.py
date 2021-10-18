"""Test for invert function."""

__author__ = "730463762"

from exercises.ex06.dictionaries import invert


def test_invert_empty() -> None:
    """Tests a function with an empty list."""
    book: dict[str, str] = {}
    assert invert(book) == {}
    return None


def test_invert_one_key() -> None:
    """Tests a function that has multiple original values."""
    book: dict[str, str] = {"one": "1"}
    assert invert(book) == {"1": "one"}
    return None


def test_invert_natural_numbers() -> None:
    """Tests the invert function with natural numbers."""
    book: dict[str, str] = {"one": "1", "two": "2", "three": "3"}
    assert invert(book) == {"1": "one", "2": "two", "3": "three"}
    return None