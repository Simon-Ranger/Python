# Created by Simon Ranger : November 17th 2022

"""
This is a basic program about letting the user create their own story that will randomise into something completely
different each time.

How to Play:
1. Enter a sentence, can be however long when prompt

Desired Output:
To have a random generated story appear each time the script is run, but using user inputs to finish some
story.
"""

import random

if __name__ == "__main__":
    startingSentence = f"Many years ago there was a "
    story = [input("Enter a character for the story: "),
             input("Enter what the character is doing: "), input("Enter what time or period it is: "),
             input("Enter how old the character is: "), input("Enter where the story takes place: ")]

    random.shuffle(story)

    print(f"Your created story is...\n{startingSentence}")

    for sentence in story:
        print(f"{sentence}")



