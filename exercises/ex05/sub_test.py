"""Test for sub function."""

__author__ = "730463762"

from exercises.ex05.utils import sub


def test_sub_empty_list() -> None:
    """Tests sub function with an empty list."""
    line: list[int] = []
    assert sub(line, 1, 4) == []
    return None


def test_sub_negative_start() -> None:
    """Tests sub function with a negative start point."""
    line: list[int] = [10, 20, 30, 40, 50]
    assert sub(line, -5, 4) == [10, 20, 30, 40]
    return None


def test_sub_larger_end() -> None:
    """Tests sub function with a end out of range."""
    line: list[int] = [10, 20, 30, 40, 50]
    assert sub(line, 0, 6) == [10, 20, 30, 40, 50]
    return None


def test_sub_count_by_tens() -> None:
    """Tests the sub function with a full list and both paramters are natural numbers."""
    line: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    assert sub(line, 2, 8) == [30, 40, 50, 60, 70, 80]
    return None