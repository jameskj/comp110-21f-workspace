"""Using Function Definitions to Find Duplicate Letters in Words."""

__author__ = "730463762"

words: str = input("Enter a word: ")
length: int = len(words) - 1
default: bool = False


def duplicate(a: str, b: int, c: bool) -> bool:
    """Checking for Multiples."""
    counter = 0
    check = " "
    while counter <= b: 

        if a[counter] in check:
            c = True
            return c
        
        check = check + a[counter]
        counter = counter + 1
        
    return c


last: bool = duplicate(words, length, default)
print("Found duplicate: " + str(last))