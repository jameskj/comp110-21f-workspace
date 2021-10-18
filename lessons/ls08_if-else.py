"""Practicing If-Else Statements."""

__author__ = "730463762"


SECRET = int(4)
print("Pick a number, one through five.")
guess = int = int(input("What is your guess?"))

if guess == SECRET:
    print("Good job! You got it right!")

else:
    print("Sorry, that is incorrect!")

    if guess > SECRET:
        print("You guessed too high!")
    
    else: 
        print("You guessed too low!")

print("Game over!")