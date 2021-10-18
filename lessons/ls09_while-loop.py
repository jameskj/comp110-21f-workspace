"""Practicing While Statements."""

__author__ = "730463762"

counter: int = 0
maximum: int = int(input("What is going to be the highest number we count to?"))

while counter <= maximum:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("Done!")
