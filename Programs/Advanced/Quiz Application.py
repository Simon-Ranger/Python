# Created Simon Ranger : December 10th 2022

"""
This is a fun project at a more advanced level where it consists of a quiz application.

How to Play:
1. Read the question in the output
2. Answer the questions best you can

Desired Output:
The user will be given several question styles including multiple choice and true or false, the application will find
the question and answer within the question files based on the question ID's, presents the user with feedback once the
question has been answered (if they got it correct or not).
"""

# Imports Needed
from pandas import DataFrame
from QuizApplicationDatabase import *


# Define the main menu
def mainMenu():
    # give the user a choice of multiple choice or true/false and choice to exit the program
    choice = int(input("\nPlease select from the options below:\n1. Multiple Choice Quiz\n2. True or False Quiz\n3. "
                       "Exit"))

    # perform the action depending on user selection
    if choice == "1":
        multipleChoice()
    elif choice == "2":
        trueFalse()
    elif choice == "3":
        exit(f"Thank you {name} for playing")


# Define the multiple choice questions
def multipleChoice():
    pass

    # opening message
    print(f"Welcome {name} to the multiple choice section of the program, hope you enjoy yourself and good luck!")

    # grab the questionID and question text from database

    # randomly select questions from the list

    # get the users answer and check it with the correct answer

    # put in error handling for wrong input type

    # give the overall feedback to the user, how many they got right


# Define the true or false questions


def trueFalse():
    pass

    # opening message
    print(f"Welcome {name} to the true or false section of the program, hope you enjoy yourself and good luck!")

    # grab the questionID and question text from database

    # randomly select questions from the list

    # get the users answer and check it with the correct answer

    # put in error handling for wrong input type

    # give the overall feedback to the user, how many they got right


# saving everything to a file and outputting it in table format


if __name__ == "__main__":
    # message welcoming the user
    name = str(input(f"Please enter your name: "))
    print(f"Welcome {name} to the Quiz Master main menu")
