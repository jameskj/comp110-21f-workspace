"""Using while loops to count letters in Strings."""

__author__ = "730463762"


find_letter: str = input("What letter do you want to seach for?:")
word: str = input("Enter a word:")

counter = 0
letter_counter = 0

while counter < len(word):
    if find_letter == word[counter]:
        letter_counter = letter_counter + 1
        counter = counter + 1
    else:
        counter = counter + 1

print("Count: " + str(letter_counter))