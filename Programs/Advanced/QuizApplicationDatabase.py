"""
Contains the full database for Quiz Application.py
"""

# importing the database
from databases import Database as db

# connecting to the database
database = db(r"sqlite+aiosqlite://quiz.db")
await db.connect()

# creating the database tables
multiplechoice = """
CREATE TABLE questions (QuestionID INT PRIMARY KEY, Question VARCHAR(100), Options VARCHAR(200), Answer VARCHAR(2))
"""
await db.execute(query=multiplechoice)

# inserting the data
multiplechoice = """
INSERT INTO questions(QuestionID, Question, Options, Answer) VALUES(:QuestionID, :Question, :Options, :Answer)
"""
values = [
    {"QuestionID": 1, "Question": "do dict comprehensions exist?", "Options": "yes, no, not in python, none of the "
                                                                              "above", "Answer": "a"},
    {"QuestionID": 2, "Question": "what does the @ symbol do in python?", "Options": "adds to a list, closes the "
                                                                                     "program, call a generator, "
                                                                                     "matrix multiplication",
     "Answer": "c, d"},
    {"QuestionID": 3, "Question": "what does the secret antigravity module do in python?", "Options": "creates a "
                                                                                                      "database, "
                                                                                                      "compile the "
                                                                                                      "script, "
                                                                                                      "open a web "
                                                                                                      "page of jokes, "
                                                                                                      "none of the "
                                                                                                      "above",
     "Answer": "c, d"},
    {"QuestionID": 4, "Question": "how to do you compile in python?", "Options": "by running it in terminal, python "
                                                                                 "is interpreted, downloading an "
                                                                                 "extension, importing a module",
     "Answer": "b"},
    {"QuestionID": 5, "Question": "what is the index of the first element in a list in python?", "Options": "1,2,8,0",
     "Answer": "d"},
    {"QuestionID": 6, "Question": "can you use ; in python?", "Options": "no, yes, only on saturdays, all the above",
     "Answer": "a"},
    {"QuestionID": 7, "Question": "can you run python on the web?", "Options": "not at all, absolutely, I don't have "
                                                                               "a computer, yes but only once a "
                                                                               "year", "Answer": "b"},
    {"QuestionID": 8, "Question": "what does . . . Do?", "Options": "jump to the next step, makes the script run "
                                                                    "faster, creates a loop, nothing", "Answer": "d"},
    {"QuestionID": 9, "Question": "what does | do in python?", "Options": "separates a search in regex, bitwise OR "
                                                                          "operator, makes a new line, "
                                                                          "exits the script", "Answer": "a, b"},
    {"QuestionID": 10, "Question": "what is PEP?", "Options": "a drug, food, a python module, an official python "
                                                              "document", "Answer": "d"},
    {"QuestionID": 11, "Question": "when do you use type hinting?", "Options": "when working with functions, when "
                                                                               "doing for loops, never, they aren't "
                                                                               "in python", "Answer": "a"},
    {"QuestionID": 12, "Question": "where can you use an else statement?", "Options": "on its own, in a list or "
                                                                                      "dictionary, loops and if "
                                                                                      "statements, all the above",
     "Answer": "c"},
    {"QuestionID": 13, "Question": "Try blocks contain code that does what?", "Options": "installs packages, provides "
                                                                                         "easy access to single "
                                                                                         "instances, nothing, "
                                                                                         "gives access to a specific "
                                                                                         "range of index elements",
     "Answer": "b, d"},
    {"QuestionID": 14, "Question": "How would you put something in to a list?", "Options": "add,delete,insert,fetch",
     "Answer": "a"},
    {"QuestionID": 15, "Question": "How would you get the user to interact with the code?", "Options": "use the "
                                                                                                       "input() "
                                                                                                       "method, "
                                                                                                       "ask them "
                                                                                                       "politely, "
                                                                                                       "you can't, "
                                                                                                       "can only do "
                                                                                                       "it in C",
     "Answer": "a"}
]
await db.execute_many(query=multiplechoice, values=values)
