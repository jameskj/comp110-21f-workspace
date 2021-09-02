"""Using Random Numbers to make a Cookie Maker Simulator."""

__author__ = "730463762"

from random import randint
cookie_number: int = randint(1, 4)

print("Your fortune cookie says...")

if cookie_number < 3:
    if cookie_number == 1:
        print("You cannot love life until you live the life you love.")
    else:
        print("If you feel you are right, stand firmly by your convictions.")
else:
    if cookie_number == 3:
        print("A stranger, is a friend you have not spoken to yet.")
    else:
        print("Wealth awaits you very soon.")

print("Now, go spread positive vibes!")
