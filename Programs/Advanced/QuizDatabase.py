# Created Simon Ranger : December 10th 2022

"""
Contains the full database for QuizMaster.py

Goal of the database:
store the data for QuizMaster including:
username of whoever takes the quiz
ID of the questions
text of the questions
answer for the questions
how long it took to complete the quiz
"""

# importing the database
import sqlite3
from sqlite3 import Error, Connection
import time as t


def createConnection() -> Connection:
    # setting up the connection
    try:
        connect = sqlite3.connect(r"C:\Users\General\Desktop\Codes\Python\Programs\Advanced\QuizDatabase.db")
        connect.cursor()
        return connect
    except Error as e:
        print(e)


def creatingTable(connect, table):
    try:
        connecting = connect.cursor()
        connecting.execute(table)
    except Error as e:
        print(e)


def main() -> tuple:

    # creating the database tables
    multiplechoice = """
    CREATE TABLE IF NOT EXISTS questions (
    User TEXT NOT NULL,
    QuestionID INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL,
    Start_time TEXT,
    End_time TEXT
    )
    """

    truefalse = """
    CREATE TABLE IF NOT EXISTS questions (
    User TEXT NOT NULL,
    QuestionID INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL,
    Start_time TEXT,
    End_time TEXT
    )
    """

    # inserting the data for the tables
    multiplechoicedata = """
    INSERT INTO questions (
    User,
    QuestionID,
    Question,
    Answer,
    Start_time,
    End_time
    )
    """

    values = [
        {
            "QuestionID": 1,
            "Question": "do dict comprehensions exist?",
            "Options": "yes, no, not in python, none of the above",
            "Answer": "a",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 2,
            "Question": "what does the @ symbol do in python?",
            "Options": "adds to a list, closes the program, call a generator, matrix multiplication",
            "Answer": "c, d",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 3,
            "Question": "what does the secret antigravity module do in python?",
            "Options": "creates a database, compile the script, open a web page of jokes, none of the above",
            "Answer": "c, d",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 4,
            "Question": "how to do you compile in python?",
            "Options": "by running it in terminal, python is interpreted, downloading an extension, importing a module",
            "Answer": "b",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 5,
            "Question": "what is the index of the first element in a list in python?",
            "Options": "1,2,8,0",
            "Answer": "d",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 6, "Question": "can you use ; in python?",
            "Options": "no, yes, only on saturdays, all the above",
            "Answer": "a",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 7,
            "Question": "can you run python on the web?",
            "Options": "not at all, absolutely, I don't have a computer, yes but only once a year",
            "Answer": "b",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 8,
            "Question": "what does . . . Do?",
            "Options": "jump to the next step, makes the script run faster, creates a loop, gives access to elements",
            "Answer": "d",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 9,
            "Question": "what does | do in python?",
            "Options": "separates a search in regex, bitwise OR operator, makes a new line, exits the script",
            "Answer": "a, b",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 10,
            "Question": "what is PEP?",
            "Options": "a drug, food, a python module, an official python document",
            "Answer": "d",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 11,
            "Question": "when do you use type hinting?",
            "Options": "when working with functions, when doing for loops, never, they aren't in python",
            "Answer": "a",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 12,
            "Question": "where can you use an else statement?",
            "Options": "on its own, in a list or dictionary, loops and if statements, all the above",
            "Answer": "c",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 13,
            "Question": "Try blocks contain code that does what?",
            "Options": "installs packages, tests the code, nothing, runs exceptions",
            "Answer": "b, d",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 14,
            "Question": "How would you put something in to a list?",
            "Options": "add,delete,insert,fetch",
            "Answer": "a",
            "Start_time": "",
            "End_time": ""
        },

        {
            "QuestionID": 15,
            "Question": "How would you get the user to interact with the code?",
            "Options": "use the input() method, ask them politely, you can't, can only do it in C",
            "Answer": "a",
            "Start_time": "",
            "End_time": ""
        }
    ]

    # connecting tables with database
    connection = createConnection()

    if connection:
        creatingTable(connection, multiplechoice)
        creatingTable(connection, multiplechoicedata)
    else:
        print(f"Something went wrong...No connection made!")

    return multiplechoicedata, values


if __name__ == "__main__":
    main()
