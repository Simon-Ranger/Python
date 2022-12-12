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
from QuizDatabase import *


# Define the main menu
def mainMenu():
    # perform the action depending on user selection
    while choice:
        match choice:
            case 1:
                multipleChoice()
            case 2:
                trueFalse()
            case 3:
                exit(f"Thank you {name} for playing")
            case _:
                if choice != (1, 2, 3): print(f"Invalid input, please try again\n{choice}")


# Define the multiple choice questions
def multipleChoice():
    # opening message
    print(f"Welcome {name} to the multiple choice section of the program, hope you enjoy yourself and good luck! The"
          f"test will consist of 5 random questions.")

    # grab the questionID and question text from database

    # randomly select questions from the list

    # get the users answer and check it with the correct answer

    # put in error handling for wrong input type

    # give the overall feedback to the user, how many they got right

    # asks user what they want to do next
    select = int(input(f"Thank you {name} for taking the quiz, below are the following options:\n1. New test\n"
                       f"2. Test summary\n3. Return to main menu"))

    while select:
        match select:
            case 1:
                multipleChoice()
            case 2:
                testSummary()
            case 3:
                mainMenu()


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

    # asks user what they want to do next
    select = int(input(f"Thank you {name} for taking the quiz, below are the following options:\n1. New test\n"
                       f"2. Test summary\n3. Return to main menu"))

    while select:
        match select:
            case 1:
                trueFalse()
            case 2:
                testSummary()
            case 3:
                mainMenu()


def testSummary():
    pass


# saving everything to a file and outputting it in table format


if __name__ == "__main__":
    # message welcoming the user
    name = str(input(f"Please enter your name: "))
    print(f"Welcome {name} to the Quiz Master main menu")

    # give the user a choice of multiple choice or true/false and choice to exit the program
    choice = int(input("\nPlease select from the options below:\n1. Multiple Choice Quiz\n2. True or False Quiz\n"
                       "3. Exit\nEnter Number Here: "))


