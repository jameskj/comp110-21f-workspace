"""Test for invert function."""

__author__ = "730463762"


from exercises.ex06.dictionaries import favorite_color


def test_favorite_color_empty() -> None:
    """Testing this function with an empty list."""
    results: dict[str, str] = {}
    assert favorite_color(results) == "Empty Dictionary."
    return None


def test_favorite_color_tie() -> None:
    """Testing this function where there are multiple modes in the data."""
    results: dict[str, str] = {"Jimmy": "blue", "Jimbo": "green"}
    assert favorite_color(results) == "blue"
    return None


def test_favorite_color_regular() -> None:
    """Testing a typical set of data."""
    results: dict[str, str] = {"Alex": "blue", "Ben": "green", "Carson": "blue", "Daron": "yellow", "Frank": "purple"}
    assert favorite_color(results) == "blue"
    return None