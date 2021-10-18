"""Test for concat function."""

__author__ = "730463762"

from exercises.ex05.utils import concat


def test_concat_empty_lists() -> None:
    """Tests this function with two empty lists."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []
    return None


def test_concat_one_list_empty() -> None:
    """Tests this function with only one empty list."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = []
    assert concat(list1, list2) == [1, 2, 3]
    return None


def test_concat_two_lists() -> None:
    """Tests this function with both lists having indexes greater than 0."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]
    return None