"""Using Dictionaries for Exercise 6."""

__author__ = "730463762"


def invert(book: dict[str, str]) -> dict[str, str]:
    """Takes the key and value in a dictionary and switches them."""
    new_book = {}
    for x in book:
        new_book[book[x]] = x

    if len(book) != len(new_book):
        raise KeyError("Duplicate Keys found in New List.")
    
    return new_book


def favorite_color(results: dict[str, str]) -> str:
    """Inverts the values and then finds the most common value in the new list."""
    if len(results) < 1:
        return "Empty Dictionary."
    new_list: list[str]
    new_list = []
    for x in results:
        new_list.append(results[x])

    counter: int = 0
    color = new_list[0]
    for x in new_list:
        frequency = new_list.count(x)
        if frequency > counter:
            counter = frequency
            color = x

    return color


def count(scroll: list[str]) -> dict[str, int]:
    """Create a dictionary for frequency of objects."""
    thanks: dict[str, int] = {}

    for x in scroll:
        if x not in thanks:
            thanks[x] = 1
        else:
            thanks[x] = thanks[x] + 1
    return thanks
            