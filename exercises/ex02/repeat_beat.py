"""Using While Loops to simulate a beat box."""

__author__ = "730463762"


beat: str = input("What beat do you want to repeat?")
beat0 = beat
length: int = int(input("How many times do you want to repeat it?"))

counter: int = 1
while counter < length:
    counter = counter + 1
    beat = beat + " " + beat0
if length < 1:
    beat = "No beat..."
print(beat)