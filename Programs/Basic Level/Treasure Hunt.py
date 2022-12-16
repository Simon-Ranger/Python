# Created by Simon Ranger : November 3rd 2022

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
def intro() -> None:
    """
    The introduction to the adventure game

    Args:

    Returns:
        None
    """

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
            exit(f"You have chose to leave the treasure behind and go home!")
        else:
            print(f"Please give a valid option: ")


def firstDefender() -> None:
    """
    Presents the user with a challenger when entering the room

    Args:

    Returns:
        None
    """

    directions = ["up", "down", "right", "left"]
    print(f"OH NO! you ran into a defender of the treasure!!! Where do you run to now?")
    userinput = ""

    # Runs through the options for the user and directs them to the allocated functions based on the input
    while userinput not in directions:
        print(f"Options:\nleft\nright\nup\ndown")
        userinput = str(input('Enter a direction: '))

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


def randomHint() -> None:
    """
    Gives the user a random hit

    Args:

    Returns:
        None
    """

    directions = ["up", "down", "left"]
    print(f"The treasure is somewhere below!")
    userinput = ""

    # Runs through the options for the user and directs them to the allocated functions based on the input
    while userinput not in directions:
        print(f"Options:\nleft\nup\ndown")
        userinput = input('Enter a direction: ')

        if userinput == "up":
            emptyRoom()
        elif userinput == "left":
            firstDefender()
        elif userinput == "down":
            winner()


def emptyRoom() -> None:
    """
    Sends the user a message when entering an empty room, giving them more path options as well

    Args:

    Returns:
        None
    """

    directions = ["up", "down", "left", "right"]
    print(f"Oh no there is nothing here....")
    userinput = ""

    # What happens when the user enters an empty room
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


def winner() -> None:
    print(f"Congratulation...You escaped with the treasure!")


if __name__ == "__main__":
    while True:
        # Displays how to play the game
        print(f"How to Play:\n1. Move through different rooms\n2. Read the clues given\n"
              f"3. Find the treasure and finish the game\n")

        print(f"{'Starting game':#^65}")

        # Welcome message for the user
        print(f"Welcome to the Treasure Hunt!\nAs we do love treasure you have decided to go look for some!\n"
              f"However you found yourself inside a maze of rooms!!!\nTo get the treasure and escape the maze you have "
              f"follow the clues by moving in multiple directions.\nWhat is your name young adventurer: ")

        name = input()

        print(f"Enjoy exploring and good luck {name}!")

        intro()
