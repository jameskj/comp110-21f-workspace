"""Using While Loops to make Rows of Trees."""

__author__ = "730463762"

depth: int = int(input("Depth: "))
counter = 1
trees: str = ""
emoji = str = "\U0001F332"

while counter <= depth:
    if depth > 0: 
        trees = trees + emoji
        print(trees)
        counter = counter + 1
