"""
This is a basic but fun number guessing game that the user can play with.

How to Play:
1. Guess a number between 1 and 20
2. Follow the hints given if guess was wrong
3. After 5 fails you lose the game

Desired Output:
If working correctly the user should get a hint for every wrong answer until they get it right or lose
the game.
"""
import random


# The rules to the game
def rules():
    print(f"How to Play:\n1. Guess a number between 1 and 10\n2. Follow the hints given if guess was wrong\n"
          f"3. After 4 fails you lose the game")


def game():
    # Welcomes the user
    print(f"Welcome to my Number Guessing game!")

    # Setting the max number
    highest = 10

    # Setting a limit amount of tries
    limit = 3

    # Setting the answer
    ans = random.randrange(1, highest)
    user = 0
    count = 0

    # Running the game
    while user != ans:
        user = int(input('Please enter a number: '))

        if count == limit:
            exit(print(f"Sorry you have no more tries left"))
        elif user == ans:
            print(f"Congratulations, you got it! The answer was {user}")
            break
        else:
            if user < ans:
                print(f"Try guessing higher")
            else:
                print(f"Try guessing lower")

            count = count + 1


# Calling rules and game
rules()
game()
