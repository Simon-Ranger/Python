# Created by Simon Ranger : November 23rd 2022

"""
This is a VERY basic dice game where the user can try and guess what the dice will roll

How to Play:
1. Run the script
2. Follow the prompts

Desired Output:
The user should be able to have 5 rolls of the dice against the computer with the results being displayed at the end
"""

# Imports required
import random

# Setting the players score
user: int = 0
computer: int = 0

# Rolling the dice 5 times
for i in range(5):

    # Creating the dice
    user_dice = random.randint(1, 6)
    computer_dice = random.randint(1, 6)

    # Displaying the results of the rolls
    print(f"An Example Roll:\nPlayer 1 rolled: {user_dice}\nPlayer 2 rolled: {computer_dice}")

    # Deciding who won based on the dice rolls
    if user_dice > computer_dice:
        print(f"You win!")
        user = user + 1
    elif user_dice < computer_dice:
        print(f"Computer wins :(")
    elif user_dice == computer_dice:
        computer = computer + 1
        print(f"It's a draw!!!")

    input('\nChoose a number to start: ')

# When the game ends
print(f"The game has now ended...\nPlayer 1's score is: {user}\nPlayer 2's score is: {computer}")