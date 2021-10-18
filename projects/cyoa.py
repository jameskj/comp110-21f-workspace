"""Creating my own adventure for project 1."""

__author__ = "730463762"

# Declaring Global Variables for the game.
points: int = 0
player: str
game_name: str = "Game of Magic Doors"
forfeit: int = 1
choice: int
objective: int
counter: int = 1

UNICORN: str = "\U0001F984"
BUCKET: str = "\U0001F4A7"
MEDAL: str = "\U0001F3C5"
EYES: str = "\U0001F440"
TREE: str = "\U0001F384"


# The following is my main function in the game.
def main() -> None:
    """Main Function that Runs in the program!"""
    global choice
    global counter
    global objective
    from random import randint
    any_one: int = int(randint(1, 5))
    # The Greet function will provide an explanation of the game.
    greet()
    # The Door1 function provides the first riddle of the game.
    goal()
    choice = any_one

    if choice == 1:
        door1(points)

    elif choice == 2:
        door2(points)

    elif choice == 3:
        door3(points)

    elif choice == 4:
        door4(points)

    elif choice == 5:
        door5(points)

    while forfeit == 1 and counter <= 4:
        choice = int(input("You can choose Room 1, Room 2, Room 3, Room 4, or Room 5. \nWhich room will you choose?"))
        if choice == 1:
            door1(points)
            counter = counter + 1

        elif choice == 2:
            door2(points)
            counter = counter + 1

        elif choice == 3:
            door3(points)
            counter = counter + 1

        elif choice == 4:
            door4(points)
            counter = counter + 1

        elif choice == 5:
            door5(points)
            counter = counter + 1

        else:
            print("You did not select a valid room, please try again!")

        if counter == 4:
            print("This is your final room, make this one count!")
    if points >= objective:
        print(f"Good job {player}! You successfully met your goal of getting {objective} adventure points. \nYou finished the game with {points} adventure points! Thanks for playing, please come play again again!")
    else:
        print(f"Hey {player}, unfortunately, you did not meet you goal of getting {objective} adventure points. \nYou came up short only getting {points} adventure points. Thanks for playing, please come play again again!")


# The following procedure establishes a goal in the game!
def goal() -> None: 
    """This is where the player will set their own goals."""
    print("To measure your success in this game, you will set a goal for your adventure points.")
    global objective
    objective = int(input("What would you like your goal to be for adventure points?"))
    print(f"You have selected your goal to be {objective} adventure points")
    return None


# The following procedure gives an introduction to the game!
def greet() -> None:
    """This asks the players name and gives them a welcome message."""
    global player
    player = str(input("What is your name?"))
    print(f"Hey {player}, Welcome to my {game_name}.\nIn this game, you will make a series of choices going through many different doors.\nAs the game continues, you will be rewarded adventure points.")
    print("At the beginning of each round, you can select a new room to go into. \nYou can redo rooms if you would like!")
    print("To start off the game, a random room will be chosen. \nThen, you will choose four subsequential rooms.\nGood luck in the game!")
    return None


# The following function provides the first room.
def door1(a: int) -> int:
    """Room 1."""
    global points
    global forfeit
    # Give the first Riddle.
    print(f"This riddle states:\n'You can see me, but I weigh nothing.\nIf you put me in a bucket of water {BUCKET}, I'll make it lighter.'\nWhat am I?")
    # Give options for the riddle.
    print("Door 1 says 'A mop' \nDoor 2 says 'Air' \nDoor 3 says 'A hole' \nIf you would like to turn back and end the game, enter '0'.")
    answer1: int = int(input("Which door will you select? "))
    if answer1 <= 3 and answer1 > 0: 
        if answer1 == 1:
            print("Sorry, that is incorrect. \nYou will recieve no adventure points.")
            print(f"You currently have {a} Adventure Points.")
            points = a
            return a

        else:
            if answer1 == 2:
                print("Sorry, that is incorrect. \nYou will recieve no adventure points.") 
                print(f"You currently have {a} Adventure Points.")
                points = a
                return a 

            else: 
                print("Good job, that is correct. \nYou will recieve three adventure points.")
                a = a + 3
                print(f"You currently have {a} Adventure Points.")
                points = a
                return a
                
    else:
        if answer1 == 0:
            print(f"Thank you for playing, you finished with {a} adventure points.")
            points = a
            forfeit = 0
            return a

        else:
            print("You did not select a vaild door. Going to the next room.")
            print(f"You currently have {a} Adventure Points.")
            points = a
            return a


# The following function provides the second room.
def door2(b: int) -> int:
    """Second Question function."""
    global forfeit
    global points
    print(f"This question states:\nHow many countries have not missed one of the modern-day Olympics {MEDAL}?")
    answer2 = int(input("Door 1 says 'Two Nations' \nDoor 2 says 'Three Nations' \nDoor 3 says 'Four Nations' \nIf you would like to turn back and end the game, enter '0'. \nWhich door will you select?"))
    if answer2 <= 3 and answer2 > 0: 
        if answer2 == 1:
            print("Good job, that is correct. \nYou will recieve three adventure points.")
            b = b + 3
            print(f"You currently have {b} Adventure Points.")
            points = b
            return b

        else:
            if answer2 == 2:
                print("Sorry, that is incorrect. \nYou will recieve no adventure points.") 
                print(f"You currently have {b} Adventure Points.")
                points = b
                return b

            else: 
                print("Sorry, that is incorrect. \nYou will recieve no adventure points.")
                print(f"You currently have {b} Adventure Points.")
                points = b
                return b

    else:
        if answer2 == 0:
            print(f"Thank you for playing, you finished with {b} adventure points.")
            points = b
            forfeit = 0
            return b

        else:
            print("You did not select a vaild door. Going to the next room.")
            print(f"You currently have {b} Adventure Points.")
            points = b
            return b


# The following function provides the third room in the game.
def door3(c: int) -> int:
    """Gives the third question!"""
    global forfeit
    global points
    print(f"This question states:\nThe unicorn {UNICORN} is the national animal of which nation?")

    answer3 = int(input("Door 1 says 'Scotland' \nDoor 2 says 'Wales' \nDoor 3 says 'Cyprus' \nIf you would like to turn back and end the game, enter '0'. \nWhich door will you select?"))
    if answer3 <= 3 and answer3 > 0: 
        if answer3 == 1:
            print("Good job, that is correct. \nYou will recieve three adventure points.")
            c = c + 3
            print(f"You currently have {c} Adventure Points.")
            points = c
            return c

        else:
            if answer3 == 2:
                print("Sorry, that is incorrect. \nYou will recieve no adventure points.") 
                print(f"You currently have {c} Adventure Points.")
                points = c
                return c

            else: 
                print("Sorry, that is incorrect. \nYou will recieve no adventure points.")
                print(f"You currently have {c} Adventure Points.")
                points = c
                return c

    else:
        if answer3 == 0:
            print(f"Thank you for playing, you finished with {c} adventure points.")
            points = c
            forfeit = 0
            return c

        else:
            print("You did not select a vaild door. Going to the next room.")
            print(f"You currently have {c} Adventure Points.")
            points = c
            return c


# The following function provides the fourth room.
def door4(d: int) -> int:
    """Gives the fourth question!"""
    global forfeit
    global points
    print(f"This riddle states:\nWhat is something that you are forever leaving behind, but still always have? {EYES}")

    answer4 = int(input("Door 1 says 'Smell' \nDoor 2 says 'Fingerprints' \nDoor 3 says 'Memory' \nIf you would like to turn back and end the game, enter '0'. \nWhich door will you select?"))
    if answer4 <= 3 and answer4 > 0: 
        if answer4 == 1:
            print("Sorry, that is incorrect. \nHowever, you will recieve one adventure point for creativity.")
            d = d + 1
            print(f"You currently have {d} Adventure Points.")
            points = d
            return d

        else:
            if answer4 == 2:
                print("Good job, that is correct. \nYou will recieve three adventure points.") 
                d = d + 3
                print(f"You currently have {d} Adventure Points.")
                points = d
                return d

            else: 
                print("Sorry, that is incorrect. \nYou will recieve no adventure points.")
                print(f"You currently have {d} Adventure Points.")
                points = d
                return d

    else:
        if answer4 == 0:
            print(f"Thank you for playing, you finished with {d} adventure points.")
            points = d
            forfeit = 0
            return d

        else:
            print("You did not select a vaild door. Going to the next room.")
            print(f"You currently have {d} Adventure Points.")
            points = d
            return d


# The following function provides the fifth and final room in the game!
def door5(e: int) -> int:
    """Gives the fifth option."""
    global forfeit
    global points
    print(f"This riddle states:\nWhat is never borrowed, but often returned? {TREE}")

    answer5 = int(input("Door 1 says 'A Gift' \nDoor 2 says 'A Thanks' \nDoor 3 says 'A check' \nIf you would like to turn back and end the game, enter '0'. \nWhich door will you select?"))
    if answer5 <= 3 and answer5 > 0: 
        if answer5 == 1:
            print("Sorry, that is incorrect. \nHowever, you will recieve one adventure point for creativity.")
            e = e + 1
            print(f"You currently have {e} Adventure Points.")
            points = e
            return e

        else:
            if answer5 == 2:
                print("Good job, that is correct. \nYou will recieve three adventure points.") 
                e = e + 3
                print(f"You currently have {e} Adventure Points.")
                points = e
                return e

            else: 
                print("Sorry, that is incorrect. \nWhat were you thinking? You will lose one adventure point.")
                e = e - 1
                print(f"You currently have {e} Adventure Points.")
                points = e
                return e

    else:
        if answer5 == 0:
            print(f"Thank you for playing, you finished with {e} adventure points.")
            points = e
            forfeit = 0
            return e

        else:
            print("You did not select a vaild door. Going to the next room.")
            print(f"You currently have {e} Adventure Points.")
            points = e
            return e


# This automatically starts the main function. 
if __name__ == "__main__":
    main()