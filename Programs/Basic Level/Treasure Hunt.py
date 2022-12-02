"""
This is a basic text-based style game the user can interact with!

How to Play:
1. Move through various rooms
2. Read the clues given
3. Find the treasure and finish the game

Desired Output:
With this game the goal is to let the user go through different rooms getting a different text box message each time,
finally congratulating them on reaching the end. To finish the game they have to find the treasure.
"""


# The start of the game
def intro():
    directions = ["up", "down", "right", "left"]
    print(f"You have just entered the maze, there are 4 doors on each side, which door will you open?")
    userinput = ""

    # Lets the player choose directional options
    while userinput not in directions:
        print(f"Options:\nleft\nright\nup\ndown")
        userinput = input('Enter a direction: ')

        if userinput == "left":
            firstDefender()
        elif userinput == "right":
            randomHint()
        elif userinput == "up":
            emptyRoom()
        elif userinput == "down":
            # Will close the program after printing a message
            exit(print(f"You have chose to leave the treasure behind and go home!"))
        else:
            print(f"Please give a valid option: ")


# A random character defending the treasured path
def firstDefender():
    directions = ["up", "down", "right", "left"]
    print(f"OH NO! you ran into a defender of the treasure!!! Where do you run to now?")
    userinput = ""

    while userinput not in directions:
        print(f"Options:\nleft\nright\nup\ndown")
        userinput = input('Enter a direction: ')

        if userinput == "left":
            randomHint()
        elif userinput == "up":
            print(f"Oh no....you ended back at the start!")
            intro()
        elif userinput == "right":
            emptyRoom()
        elif userinput == "down":
            winner()
            exit()


# A hint for the user to use in helping finish the game
def randomHint():
    directions = ["up", "down", "left"]
    print(f"The treasure is somewhere below!")
    userinput = ""

    while userinput not in directions:
        print(f"Options:\nleft\nup\ndown")
        userinput = input('Enter a direction: ')

        if userinput == "up":
            emptyRoom()
        elif userinput == "left":
            firstDefender()
        elif userinput == "down":
            winner()


# What happens when the user enters an empty room
def emptyRoom():
    directions = ["up", "down", "left", "right"]
    print(f"Oh no there is nothing here....")
    userinput = ""

    while userinput not in directions:
        print(f"Options:\nleft\nup\ndown")
        userinput = input('Enter a direction: ')

        if userinput == "up":
            emptyRoom()
        elif userinput == "left":
            firstDefender()
        elif userinput == "right":
            randomHint()
        elif userinput == "down":
            winner()


def winner():
    print(f"Congratulation...You escaped with the treasure!")


if __name__ == "__main__":
    while True:
        print(f"How to Play:\n1. Move through different rooms\n2. Read the clues given\n"
              f"3. Find the treasure and finish the game\n")

        print(f"{'Starting game':#^65}")

        print(f"Welcome to the Treasure Hunt!\nAs we do love treasure you have decided to go look for some!\n"
              f"However you found yourself inside a maze of rooms!!!\nTo get the treasure and escape the maze you have "
              f"follow the clues by moving in multiple directions.\nWhat is your name young adventurer: ")

        name = input()

        print(f"Enjoy exploring and good luck {name}!")

        intro()
