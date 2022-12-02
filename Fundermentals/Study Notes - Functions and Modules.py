"""
This file contains in the following order:
1. Functions:
    Creating and Calling
    Arguments of a Function
    Number of Arguments
    Key Arguments
    Arbitrary and Key Arguments (*args)
    Default Parameter Value
    Passing and Returning Lists
    Recursion
2. Modules:
    Creating and Using
    Variables and Renaming
    Built-in, Dir and From
    Main and Packages
3. Exercise
"""

#######################################################################################################################
#                                                      FUNCTIONS                                                      #
#######################################################################################################################
"""
Functions are bits of the program that can be reused throughout the code, it allows the naming of statement blocks,
letting you run the specified block anywhere in the program countless times.
"""

############################################### Creating and Calling ##################################################
print(f"\n{'Creating and Calling a Function':#^65}")


def new_function():  # "def" is what's used to define the function
    print(f"Printing our 1st function!")


new_function()  # use the created function with () to call it otherwise it won't run

############################################### Arguments of a Function ###############################################
print(f"\n{'Arguments of a Function':#^65}")
"""Used to pass information into functions"""


def new_function(name):  # "self" is the argument, multiple arguments can be used with a "," between them
    print("Using normal print ----> " + name + " Ranger")  # "self" is passed as the 1st self when the script is run
    print(f"Using f-string now ----> {name} Ranger")


new_function("Simon")  # calls the function with "Simon" being the "self" argument being passed

############################################### Number of Arguments ###################################################
print(f"\n{'Number of Arguments':#^65}")
"""
Functions has to have the exact amount of arguments being called that are being passed. If anything other than 2
arguments are called it will give an error as we are passing 2 arguments, if it was 1 or whatever number than only that
specific number has to be called.
"""


def new_function(fname, lname):
    print("Using reg print you need to have ' ' to make a space! ----> " + fname + " " + lname)
    print(f"With f-string you don't need the ' ' ----> {fname} {lname}")


new_function("Simon", "Ranger")

################################################ Key Arguments ########################################################
print(f"\n{'Key Arguments':#^65}")
"""Used to make the order of the arguments invalid"""


def new_function(book2, book1, book3):
    print("I am reading a ----> " + book1 + " <---- book using regular print!")
    print(f"I am now reading ----> {book2} and {book3} <---- books lately using f-string!")


new_function(book1="action", book2="fantasy", book3="romance")

############################################### Arbitrary and Key Arguments (*args) ###################################
print(f"\n{'*args and **kargs':#^65}")
"""
Putting * before the argument will get a tuple of arguments which can be accessed when needed, this is great when
not knowing how many arguments could be in the function.
"""


def new_function(*books):
    print("I like to read ----> " + books[0] + " <---- books using reg print!")
    print(f"However I prefer to read ----> {books[1]} <---- books using f-string!")


new_function("action", "fiction", "romance")

"""This is almost the same as *args but will get a dictionary of arguments instead of a tuple."""


def new_function(**name):
    print("My self is " + name["fname"] + " " + name["lname"] + " and I am using reg print for this!")
    print(f"My self is {name['fname']} {name['lname']} and I'm using f-string for this!")


new_function(fname="Simon", lname="Ranger")

############################################### Default Parameter Value ###############################################
print(f"\n{'Default Parameter Value':#^65}")


def new_function(country="Australia"):
    print("I lived in ----> " + country + " <---- where they only use reg print")
    print(f"I have now moved to ----> {country} <---- where f-string is the way to go!")


new_function()  # without an argument the default "Korea" argument will be used
new_function("Korea")

############################################### Passing and Returning Lists ###########################################
print(f"\n{'Passing and Returning Lists':#^65}")
"""
Lets you send any argument data type to a function while still being treated as the same data type inside the
function. Making a list as an argument remain a list when getting to the function.
"""


def new_function(snacks):
    print(f"Lets see what snacks we can have today~~~ ----> {[x for x in snacks]} <---- are our choices")


snacks = ["choco", "ice cream", "jelly"]

new_function(snacks)

"""Return doesn't print to the user, only shows the results to the computer, so make sure to use print as well"""


def new_function(x):
    return 10 * x  # lets the function return a value


print(f"Since return doesn't show anything we have to print it manually, lets try 10 x 10 to get ----> "
      f"{new_function(10)}")


# checking if a password is correct by getting it repeated
def checking_code(code=input('Enter Code: '), repeat=input('Please Enter Code Again: ')):
    if code == repeat: print(f"Thank you for logging in, welcome!")


# Adding 2 inputs together to form anything they want!
def adding():
    return f"Your new sentence is ----> " \
           f"{input('What sentence did you want to change? ') + input('What did you want to add? ')}"


print(adding())

############################################### Recursion #############################################################
print(f"\n{'Recursion':#^65}")
"""
A defined function can call itself letting you loop through data to find a specific result, if used incorrectly can
cause great memory or processor power but when done correctly turns into an extremely good way to do mathematically -
elegant form of programming.
"""


# The prints will display how the recursion is broken down
def rec(a):  # will end when the condition is no longer greater than 0
    print(f"rec({a}) is called\n")
    if a > 0:
        print(f"Compute {a} + rec({a - 1})")
        r = a + rec(a - 1)  # decrements -1 each time a recurse happens
        print(f"{a} + rec({a - 1}) computes to {r}")
    else:
        print(f"termination condition: rec({a}) computes 0")
        r = 0
    print(f"rec({a}) returned {r}\n")
    return r


print(f"A breakdown of the Recursion results are:")
rec(3)

print(f"{'Recursion 2':#^65}")


def rec2(n):
    if n == 1: return 1
    if n != 1: return n * rec2(n - 1)


print(f"Another breakdown of the Recursion results are:\n"
      f"5 * rec2(4)\n5 * 4 * rec(3)\n5 * 4 * 3 * rec2(2)\n5 * 4 * 3 * 2 * 1 = {rec2(5)}")

print(f"{'Recursion 2':#^65}")


def calc(k):
    if len(k) == 0:
        return 0
    else:
        return k[0] ** 2 + calc(k[1:])


k = [1, 2, 3, 4, 5]
print(f"This uses recursion to find the sum of the squared numbers ----> {calc(k)}")

#######################################################################################################################
#                                                  MODULES                                                            #
#######################################################################################################################
"""
Not much different from a library of code, this is a file containing important data of previously created functions
that are wanting to be imported to another script. Modules can be used to import various other functions from other
scripts which can be very useful!. It is mainly used when implementing imports from the standard python library. When
importing modules from other scripts it's best to create a '.pyc file' which is a file that is byte-compressed, but make
sure the '.pyc' files are created in the same directory as the .py files otherwise it won't be created.
"""

##################################################### Creating and Using ##############################################
print(f"\n{'Creating and Using a Module':#^65}")
"""
When creating a module it is as simple as writing code and saving it to a .py file and when you want to use it
just import it to whatever code you need it for. Importing a module on its own is much better performance wise than
using the "from import" preventing clashes between modules. It should look like "import x" where "x" is whatever your
module (.py) is, then "x.a" where "a" is the function you are importing.
"""

import ModuleTest


# The function saved as ModuleTest
def testing(name):
    print(f"{name} is testing their 1st module creation!")


ModuleTest.testing("Simon")

###################################################### Variables and Renaming #########################################
print(f"\n{'Variables and Renaming':#^65}")
"""
You can have anything within the module such as dictionaries, arrays and pretty much anything else you would
normally have within a script, if you wanted to shorten the name of the file when importing use the keyword 'as'.
"""

import ModuleTest as mt  # lets you use "mt" instead of the whole name for future references

print(f"Modules can be too long so just shorten them! here we use 'mt' as the module! So...what country are we in? "
      f"----> {mt.Student['country']}")

####################################################### Built-in, Dir and From ########################################
print(f"\n{'Built-in, Dir and From Methods':#^65}")
"""
If you don't want to create your own or you just generally don't need to, there are several python modules that 
come pre-built for you to use, you'd have to look at the python documents to see them all as it's a very long list.
Python doesn't just have modules built in but also functions, such as dir() which outputs every name related to that
module. Than you have the from module letting you get specific things from the import rather than everything which
might not be needed.
"""

import platform  # provides system information

# uses dir() to search the platform module to find and list all function names within it
print(f"Ever wanted to know what function names are within your system? Find out by using the 'dir()' function. "
      f"Lets take a look shall we ---->\n{dir(platform)}\nor if we want the attribute names ----> {dir()}")

print(f"This is just using 'student' out our created module to get the age ----> {mt.Student['age']}")

####################################################### Main and Packages #############################################
print(f"\n{'Main and Packages':#^65}")
"""
The '__main__' is mainly used to find out if the module you are running is being used by another module or on its own,
letting you manipulate the module depending on the situation.
"""

if __name__ == "__main__":
    print(f"The modules used in this script are not being used by other modules!")

"""
Packages are the best way to maintain a clean order of modules within a folder with a special "__init__.py" file 
indicating to python the folder contains python modules making it special. If you want to make a package called "a"
with sub-packages "b", "c", "d" which have their own sub-packages such as "e", "f", "g" etc. the structure would look
like:

A random folder in 'sys.path'
    a/
        __init__.py
        b/
            __init__.py
            e/
                __init__.py
                file.py
        c/
            __init__.py
            f/
                __init__.py
                file.py
"""

#######################################################################################################################
#                                                 EXERCISE                                                            #
#######################################################################################################################
print(f"\n{'Exercise Practice: Converting Temperature':#^65}")

celsius = int(input('Please enter a temperature in Celsius: '))


def conv(c):
    c1 = 9 / 5 * celsius + 32
    return c1


fahrenheit = conv(celsius)
print(f"The converts temp is {fahrenheit} degrees Fahrenheit")
