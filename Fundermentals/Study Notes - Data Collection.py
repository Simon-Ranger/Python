"""
This file contains in the following order:
1. Strings:
    Assigning Strings and Variables
    Multi-Line Strings
    Using Strings as Arrays
    Slicing Strings:
        Regular
        Slicing with Negatives
        Slicing with Steps
    Modifying Strings:
        Upper and Lower Case
        Removing Whitespace
        Replacing, Splitting and Combining a String
    Formatting Strings:
        Regular String
        Multiple Value
        Index Numbers and Naming an Index
2. Escape Characters:
    Basic Escaping
    List of Escape Characters
3. Variables:
    General:
        Creating Variables
        Casting and Type
        Case Sensitive
        Variable General and Multiple Names
        Assigning Multiple Values
    Global:
        Creating a Global Variable
        The Global Keyword
4. Arrays:
    Accessing the Elements
    Finding the Length
    Adding and Removing
5. Dictionaries:
    Regular
    Nested
6. User Input
7. Exercise
"""

#######################################################################################################################
#                                                 STRINGS                                                             #
#######################################################################################################################

########################################## Assigning Strings and Variables ############################################
print(f"\n{'Assigning Strings and Variables':#^65}")
a = "Hello"  # the variable "a" now has the value "Hello" assigned to it
print(f"variable 'a' has the value ----> {a}")

########################################## Multi-Line Strings #########################################################
print(f"\n{'Multi-Line Strings':#^65}")
"""
This print function using an additional 2 " at the start and end of the String will turn it into something called
a multi-line String. 
"""
print(f"Showing ways to do multi-line Strings:")
print("""Relearning to python is a lot of fun,
I haven't coded in many years,
So I hope I still enjoy what's to come!. <---- triple quotes\n""")

print(f"Relearning to python is a lot of fun,\n"
      f"I haven't coded in many years,\n"
      f"So I hope I still enjoy what's to come!. <----- f string")

########################################## Using Strings as Arrays ####################################################
print(f"\n{'Using Strings as Arrays':#^65}")
"""
Python strings are just arrays of bytes representing unicode characters, with a single character being its own string
with a length of 1, using [] lets you access the element of the strings. 
"""
a = "Hello, There"
print(f"indexing the letter ----> {a[1]}")

#######################################################################################################################
#                                           SLICING STRINGS                                                           #
#######################################################################################################################
"""
Used to find a range of characters within a string, slicing is a little different from indexing as indexing includes
the last character while slicing doesn't, this is due to indexing referring to items and slicing referring to lists.
        +---+---+---+---+---+---+---+---+---+---+---+---+
        | H | e | l | l | o | , |   | T | h | e | r | e |
        +---+---+---+---+---+---+---+---+---+---+---+---+
Slice:  0   1   2   3   4   5   6   7   8   9   10  11  12
Index:    1   2   3   4   5   6   7   8   9   10  11  12
"""

########################################### Regular ###################################################################
print(f"\n{'Slicing Regular Strings':#^65}")
print(f"indexing characters 2 to 5 ----> {a[2:5]}")

################################### Slicing from the Start and End ####################################################
print(f"\n{'Slicing from the Start and End':#^65}")
print(f"indexing characters from 0 to 5 ----> {a[:5]}")  # nothing before the : implies starting at "0" and ends at "5"

print(f"indexing characters from 2 to 12 ----> {a[2:]}")  # starts at "2" ends at "12" but is the 13th character

########################################### Slicing with Negatives ####################################################
print(f"\n{'Slicing with Negatives':#^65}")
"""Starts the slice from the end of the string instead of the front"""
# "-5" starts from the last "e" in "There" and counts 5 characters, "-2" is where the slice ends
print(f"indexing from -5 to -2 ----> {a[-5:-2]}")

########################################### Slicing with Steps ########################################################
print(f"\n{'Slicing with Steps':#^65}")
"""
Normally steps have a default of 1 making it go through the string 1 character at a time, you can change the number
of characters it does at once.
"""
print(f"indexing from 0 to 4 containing 5 characters ---->  {a[0:5:4]}")  # changes the default step from "1" to "4"

#######################################################################################################################
#                                         MODIFYING STRINGS                                                           #
#######################################################################################################################

############################################ Upper and Lower Case #####################################################
print(f"\n{'Upper and Lower Case':#^65}")
"""Returns the string in upper case"""
print(f"making lower case to upper case ----> {a.upper()}")

"""Returns the string in lower case"""
print(f"making capital case to lower case ----> {a.lower()}")

############################################ Removing Whitespace ######################################################
print(f"\n{'Removing Whitespace':#^65}")
"""Space before or after the actual text happens and to make the code look cleaner removing it is best"""
print(f"we don't like gaps between quote marks ----> {a.strip()}")  # removes the gaps between " " and the wording

############################################ Replacing, Splitting and Combining a String ##############################
print(f"\n{'Replacing, Splitting and Combing a String':#^65}")
"""Simply just used to replace a string with another string"""
print(f"not feeling 'There' anymore so now its ----> {a.replace('There', 'World')}")  # changes "There" with "World"

"""Splits the string if the instances of the separator is found"""
print(f"tired of 1 sting? lets make it "
      f"2 ----> {a.split(',')}")  # turns the single string into separate sub-strings using the separator ","

"""Used to join multiple strings together using the + operator"""
a, b = "Hello, ", "There"  # having that space after "," will separate the follow string with a space.
print(f"decided 2 isn't good, lets add them together again! ----> {a + b}")
print(f"another way of spacing is having ' ' to get ----> {a + '' + b}")

#######################################################################################################################
#                                        FORMATTING STRINGS                                                           #
#######################################################################################################################
"""
Used to display a string as expected by formatting the data type or user input using the format() method. Placing
{} as something called a placeholder in the string will control the value for you.
"""

############################################# Regular String ##########################################################
print(f"\n{'Regular Strings':#^65}")
cost = 10
print(f"the cost will be ----> ${cost}")
print(f"hmm lets have it looking a bit fancy by using :.2f to make it decimal point "
      f"----> ${cost:.2f}")  # no need for the variable txt or the .format method, highly recommended to use f-string

############################################# Multiple Value ##########################################################
print(f"\n{'Multiple Values':#^65}")
"""Lets you add more than 1 value"""
cost, paid, change = 5, 10, 5
print(f"The item cost ----> ${cost:.2f}, I paid ----> ${paid:.2f}, so my change should be ----> ${change:.2f}")

############################################# Index Numbers and Naming an Index #######################################
print(f"\n{'Index Numbers and Naming an Index':#^65}")
"""Adding numbers inside the placeholders will ensure the value is placed in the correct placeholder"""
amount, item, cost = 10, 3, 30
print(f"To buy ----> {item} chocolates ----> ${amount:.2f} each, totaling ----> ${cost:.2f}")

name = "Simon"
print(f"My self is ----> {name}, today I met another ----> {name}")  # You can use the same index reference

"""By adding names into the placeholder you can set names, however within the () you must also pass the named values"""
food, drink = "burger", "coke"
print(f"my order is: ----> {food} and {drink}")

#######################################################################################################################
#                                        ESCAPE CHARACTERS                                                            #
#######################################################################################################################
"""
Some characters are illegal to use in python, so to get around this you'll have to use escape characters which is 
simply putting a backslash "\" with a character following it.
"""

############################################## Basic escaping #########################################################
print(f"\n{'Basic Escaping':#^65}")
txt = "Hello i am \"Simon\""  # lets you use double quotes when normally it will give an error
print(f"{txt}")

############################################## List of Escape Characters ##############################################
SingleQuote = "\""
Backslash = "\\"
NewLine = "\n"
CarriageReturn = "\r"  # works similar to \n as it creates a separate line
Tab = "\t"
Backspace = "\b"
FormFeed = "\f"  # generally used to force a page break when printing, but can be used to comment solid horizontal lines
OctalValue = "\000"  # the ints can be anything "000" is just an example but has to be 3 digits
HexValue = "\x48"  # the "48" is a hex number that represents a hex value

#######################################################################################################################
#                                               VARIABLES                                                             #
#######################################################################################################################

"""
Containers for data storage is pretty much all variables are used for.
"""

#######################################################################################################################
#                                              General                                                                #
#######################################################################################################################

######################################### Creating Variables ##########################################################
print(f"{'Creating Variables':#^65}")
"""There is no command for a variable, simply just assign a value to it"""
a = 1  # assigns the value of "1" to the variable "a"
print(f"We assigned the value {a} to the variable called 'a'")

######################################### Casting and Type ############################################################
print(f"\n{'Casting and Types':#^65}")
"""Used for specifying the data type of a variable"""
a, b, c = str(1), int(1), float(1)
a = 1
print(type(a))  # prints the type of "a"

######################################### Case Sensitive ##############################################################
print(f"\n{'Case Sensitive':#^65}")
"""Mainly used when needing multiple variables as the variables won't overwrite each other"""
a = 1
A = 2
print(f"Having the same variables {a} and {A} results in different outputs!")  # prints "a" as "1" and "A" as "2"

########################################## Variable General and Multiple Names ########################################
"""
Variables can have long or short names however there are still conditions for using them correctly, being that it 
starts with a letter or underscore "_", only contains letters, numbers and underscores. They are also case sensitive.
"""
vartest = "test"
var_test = "test"
_var_test = "test"
myTest = "test"
MYTEST = "test"
mytest1 = "test"

"""Camel, Pascal and Snake Cases, are 3 great ways to make a variable with multiple names easier to read"""
myFirstTest = "name"  # Camel, starts with all capitals except the 1st
MyFirstTest = "name"  # Pascal, each 1st letter is capital
my_first_test = "name"  # Snake, no capitals as the words are separated using the underscores

########################################## Assigning Multiple Values ##################################################
print(f"\n{'Assigning Multiple Values':#^65}")
a, b, c = "1", "2", "3"  # assigns each variable with a value "a=1, b=2, c=3"
print(a, b, c)

a = b = c = "1"  # assigns "1" to a, b and c
print(a, b, c)

nums = ["1", "2", "3"]  # unpacks the values assigned to the variables, "1" will unpack as "a", "2" is b and "3" is c
a, b, c = nums
print(a, b, c)

#######################################################################################################################
#                                                 GLOBAL                                                              #
#######################################################################################################################
"""
When a variable is outside of a function, they are considered global meaning they can be used in and outside of
functions. Having the same variable name inside the function, will run as a local (only allowed to run within that
function) variable not affecting the global variable at all.
"""

######################################### Creating a Global Variable ##################################################
print(f"\n{'Creating a Global Variable':#^65}")
a = "1"


def my_a():
    a = "2"
    print(f"I was {a}")


my_a()
print(f"Now i am {a} OH NO!")

########################################## The Global Keyword #########################################################
print(f"\n{'The Global Keyword':#^65}")
"""
Used to make a variable global even within a function, if you want to change a variable outside the function
you simply refer to the variable using the global keyword.
"""
x = "2"


def my_a():
    global x  # changes the value from "2" to "1" as assigned under it
    x = "1"


my_a()
print(f"I am {x}")

#######################################################################################################################
#                                                    ARRAYS                                                           #
#######################################################################################################################
"""
Python doesn't support arrays with any built-ins but using lists as arrays can be an alternate thing, to work with
arrays not in list form you'll need to import a library similar to NumPy library. An array is a special type of
variable which can hold multiple values at a time.
"""

################################################# Accessing the Elements ##############################################
print(f"\n{'Accessing an Element':#^65}")
books = ["Action", "Horror", "Science"]  # creates the array
print(f"We learnt alot until now, so it's time to look for elements within 'Arrays' using [] ----> "
      f"{books[0]} book <---- was selected!")

################################################# Finding the Length ##################################################
print(f"\n{'Revisiting Finding the Length':#^65}")
print(f"Curious to see how many book options we have to choose from? Just use 'len()' to find out! We have ----> "
      f"{len(books)} <---- types of books to choose from!")

################################################# Adding and Removing #################################################
print(f"\n{'Adding and Removing from Arrays':#^65}")
"""This is no different to what we did with data collectors"""
books.append("Fiction")
print(f"Want more than 3 choices? use the '.append()' function to add more to the list! now we have ----> "
      f"{len(books)} <---- types to choose from!\nLets see our full list now ----> {books}")
books.pop(2)
print(f"Added something by mistake? Let's just '.pop()' it out shall we! Science is old we don't need that anymore "
      f" ----> {books}\nnow we are back to ----> {len(books)} book <---- types to choose from!")
books.remove("Fiction")
print(f"Don't let fiction books anymore? '.remove()' them use ease! ----> {books} and now we are left with ----> "
      f"{len(books)} books <----")

#######################################################################################################################
#                                                    DICTIONARIES                                                     #
#######################################################################################################################
"""
Used to store data in pairs of key:values, doesn't allow duplicates but can be changed, they are very similar in
methods to the other 3 but written out completely differently. If you want more than 1 value you'll have to use []
otherwise it won't run. To find the length and index is the exact same lists, etc.
"""

########################################### Regular ###################################################################
print(f"\n{'Regular Dictionary':#^65}")
newdict = {
    "name": "Simon",
    "age": 32,
    "Occupation": "Teacher"
}
print(f"This is a regular dictionary, pretty simple :D ----> {newdict}")

info = input("What would you like to know? ")
print(f"The data result is ----> {newdict.get(info, 'No data found...please try again: ')}")

########################################### Nested ####################################################################
print(f"\n{'Nested Dictionary':#^65}")
"""You can have a dictionary hold multiple other dictionaries within it"""

# 3 different dictionaries within the "mystudent" dictionary
mystudent = {
    "student1": {
        "name": "Bob",
        "Age": 20
    },
    "student2": {
        "name": "Jane",
        "Age": 21
    },
    "student3": {
        "name": "James",
        "Age": 19
    }
}

# 3 separate dictionaries
student1 = {
    "name": "Bob",
    "Age": 20
}
student2 = {
    "name": "Jane",
    "Age": 21
}
student3 = {
    "name": "James",
    "Age": 19
}

# Makes the mystudent dictionary hold the 3 separate dictionaries within its own dictionary
mystudent = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}

print(f"Now we have nested dictionaries which can be very useful! ---->\n{mystudent}")

#######################################################################################################################
#                                             USER INPUT                                                              #
#######################################################################################################################
print(f"\n{'User Input':#^65}")
"""
This is one of the most fun things when it comes to programming and that is simply due to the fact that this lets your
code interact directly with the person(s) using your program!
"""

# you can do this with floats and complex formats as well
print(f"{int(input('Please put in an int number only: '))}\n")

# printing the result of multiple user inputs
x, y = int(input('First input here: ')), int(input('Second input here: '))
print(f"The result of both inputs is {x + y}\n")

# using the 'walrus operator' to make the input function more clean
print(f"{[num:= int(input('This will simply just print the number given: '))]}")

#######################################################################################################################
#                                               EXERCISE                                                              #
#######################################################################################################################
print(f"\n{'Exercise Practice: Making a Calculator':#^65}")
"""Build a calculate to add the 2 inputs together"""

# you can change the + to whatever math operator you would like
print(f"This is a very basic calculater {input('First Number: ') + input('Second Number: ')} is the answer!\n")

