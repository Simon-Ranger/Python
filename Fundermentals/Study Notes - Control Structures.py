"""
This file contains in the following order:
1. Booleans:
    Comparison
    Logic
    Evaluate Values and Variables
    Precedence
2. If, Elif and Else Statements:
    Short Hand
    Nested and Pass
3. Lists, Sets and Tuples:
    Regular Lists, Tuples and Sets
    Duplicating Lists and Tuples
    Find the Length and Type
    Creating a New List
    Changing the Value
    Changing the Range
    Functions
    Sorting and Copying
4. Loops:
    While:
        Looping Lists, Tuples and Sets
    For:
        Looping Through a String
        The range() function
        Nested Loops
        The pass statement
5. Exercise
"""

#######################################################################################################################
#                                                 BOOLEANS                                                            #
#######################################################################################################################
"""
Booleans are simply "True" or "False" expressions, you get the result by evaluating and comparing 2 different values.
"""
########################################### Comparison ################################################################
print(f"\n{'Comparing Values':#^65}")
'Used to compare multiple values'
less_than = 3 < 5  # returns if 3 is less than 5, will return True
print(f"3 is less than 5? ----> {less_than}")

more_than = 10 > 5  # returns if 10 is more than 5, will return True
print(f"10 is more than 5? ----> {more_than}")

less_or_equal = 10 <= 20  # returns if less 10 is less than or equal to 20, will return True
print(f"10 is less than or equal to 20? ----> {less_or_equal}")

more_or_equal = 10 >= 5  # returns if less 10 is more than or equal to 5, will return True
print(f"10 is more than or equal to 5? ----> {more_or_equal}")

equal = 10 == 10  # simply compares the objects to see if they are equal
print(f"10 is equal to 10? ----> {equal}")

not_equal = 10 != 5  # simply compares the objects to see if they are not equal
print(f"10 is not equal to 5? ----> {not_equal}")

########################################### Logic ##################################################################
print(f"\n{'Logical Boolean':#^65}")
"""Used to compare if the objects are within the same memory location if the objects are equal"""

print(f"Using 'and' makes it run if all conditions are ----> {12 == 12 and 10 < 12}\nUsing 'or' makes it run if only "
      f"1 condition is ----> {'five' == 'six' or 'six' > 'five'}\nUsing 'not' takes a single argument and inverts it "
      f"making what was true now ----> {not 1 < 2}\n")

# Checking someone's body heat using chained multiple conditions
heat = int(input('Please enter your body heat: '))
if 40 <= heat <= 60: print(f"You have a healthy body heat at {heat}% body heat")

"""
The and condition will be true if both values are both true, a is not equal to b making it false, while the or 
condition will show true if either of the values are true.
"""

if 1 == 1 and 1 < 2 or 2 > 1: print(f"Using Logic is a lot of fun!")

############################################## Evaluate Values and Variables ##########################################
print(f"\n{'Evaluate Values and Variables':#^65}")
"""
While most values will return True such as lists, etc. unless empty, while some will still return False such as empty
values "(), [], {}, "", 0, None and False". If you have a class with an object made from __len__ function returning 0
or False will result in returning False.
"""

print(f"is 5 less than 10? ----> {5 < 10}")  # will result in True as the statement is correct

a, b = "Hello", 4
print(f"is 'a' a string and 'b' and int? ----> {bool(a)}, {bool(b)}")

print(f"You can even use words, 'ten' > 'five'!!! ----> {'ten' > 'five'}")

########################################### Precedence ################################################################
print(f"\n{'Precedence Booleans':#^65}")
"""
This is an extension of the order of operations, letting it include multiple operators at a time.
"""

# Confirming what type a card is
card = input('What sport cards do you have? ')
if card == 'baseball' or card == 'soccer': print(f"I'll buy it!")

#######################################################################################################################
#                                                   IF ELIF ELSE                                                      #
#######################################################################################################################
print(f"\n{'If, Elif and Else':#^65}")
"""These compare the values against each other and determines the result based on the conditions used"""

a, b, c = 5, 10, 5

if a == b:
    print(f"a is equal to b")
elif a < b:  # runs when the if condition is false
    print(f"Since the check saw that '5' is < '10' it will state ----> a is less than b <---- which is a true "
          f"statement")
else:  # runs when both the if and elif conditions are false
    print(f"Both conditions were false")

############################################# Short Hand ##############################################################
print(f"\n{'Short Hand If Statement':#^65}")
"""
A simple and much more efficient way of doing it for a cleaner looking code is to have the conditions within 1 line,
this will only work if you have a single if statement though. You can't use elif in this method.
"""
age, name = int(input('Enter your age: ')), input('Enter your name: ')
if age >= 18: print(f"Welcome {name} to the club!\n")   # checks the age '18' against the input

if a < b: print(f"a is less than b")  # doesn't need an else statement
print(f"is 'a' less than 'b'? ----> '{'a' if a < b else 'b'}' <---- wow it is!")  # needs an else statement

############################################# Nested and Pass #########################################################
print(f"\n{'Nested If Statement and Pass Condition':#^65}")
"""
The nested if statement checks the 1st main if statement and than checks the following if statements under it. 
An if statement can't have an empty block of code so if for whatever reason nothing is there, the pass condition takes
its place.
"""
if b > 6:  # true so will print
    print(f"6 is less than 10")
    if b < 6:  # false so it won't print
        print(f"10 is greater than 6")
    if a != c:  # will get skipped as there is nothing under the statement
        pass  # empty block but "pass" prevents an error from happening
    else:  # will print since the previous condition was false
        print(f"6 is close to 10!")

#######################################################################################################################
#                                                LISTS, SETS AND TUPLES                                               #
#######################################################################################################################
"""
lists are simply just storage units for multiple items or values within a single variable, they are created by
using [], they can be any data type as well. When wanting to access data do the same thing as before with strings, the
same concept and method of doing so applies to lists, tuples, sets and dictionaries.
"""

######################################## Regular Lists, Tuples and Sets ###############################################
print(f"\n{'Regular Lists, Tuples and Sets':#^65}")
"""
The differences are simple, a list has [], a tuple has () and a set has {}. Tuples are also unchangeable 
meaning you can't add, remove or change them once they have been created. Sets however can't have items or the order
changed but can still have things added or removed.
"""

mylist, mytuple, myset = ["1", 2, True],  ("1", 2, True), {"1", 2, True}
print(f"lists, tuples and sets are the same except the brackets ----> {mylist}, {mytuple}, {myset}")

"""
List, tuple and set items are ordered and are able to be changed, the 1st item is indexed as [0] making "1" = [0], 2nd 
item would be "2" = [1] and "3" is [2], adding new items to the list will make it appear at the end of the list. 
You can change a list by adding or removing items even after the list has been created.
"""

######################################### Duplicating Lists and Tuples ###############################################
print(f"\n{'Duplicating Lists and Tuples':#^65}")
"""
Due to being indexed lists and tuples are able to have multiple of the same item value, however a set can't do 
this.
"""

thislist, thistuple = ["1", "2", "3", "1", "2"], ("1", "2", "3", "1", "2")
print(f"both show that '1' and '2' are allowed to be repeated ----> {thislist}, {thistuple}")

######################################### Find the Length and Type ####################################################
print(f"\n{'Finding the Length and Type':#^65}")
"""
To determine the amount of items are in a list, tuple or set, you can use the len() function which is simply just short 
for length.
"""

print(f"we can use 'len()' to find the total amount of items within a list, tuple or set ----> "
      f"{len(mylist)}, {len(mytuple)}, {len(myset)}")

"""
Python reads the data type as list and nothing else, to confirm this use the type() function.
"""

print(f"we can use 'type()' to find the type of a list, tuple or set ----> "
      f"{type(mylist)}, {type(mytuple)}, {type(myset)}")

########################################## Creating a New List ########################################################
print(f"\n{'Creating a New List':#^65}")
"""Lets you construct a list from a tuple, set or directory or anything that implements the iterable protocol"""

mylist, mytuple = list(("1", 2, True)), tuple(("1", 2, True))  # make sure to have double round brackets (())
print(f"time to make a list and tuple :O, make sure to have double round brackets though! ----> {mylist}, {mytuple}")


########################################## Changing the Value #########################################################
print(f"\n{'Changing the Value':#^65}")
"""
Refer to a specific item within the list when wanting to change the value of that item, tuples don't 
allow this.
"""
print(f"this was the original list ----> {mylist}")
mylist[1] = "blue"  # changes "2" for "blue"
print(f"by indexing a character and changing the value we can turn '2' in to ----> {mylist}")

########################################## Changing the Range #########################################################
print(f"\n{'Changing the Range':#^65}")
"""
Use indexing to specify a range of item values you want to change by referencing the index number, the amount of 
items will change if the number of inserted and replaced don't match. Tuples and sets don't allow this
"""

mylist = ["Hello", "There", "How", 1, 2, 3]
print(f"this was the original list ----> {mylist}")
mylist[1:5] = ["Bye", 4]  # "There" is replaced with "Bye" due to the "1", while "4" replaces "How, 1, 2" due to "5"
print(f"by slicing characters and changing their value we can replace"
      f"'There', 'How', '1' and '2' ----> {mylist}")

# Putting in more than taking will put the new items where specified making the current items move accordingly
mylist = ["a", "b", "c"]  # current items
print(f"this was the original list ----> {mylist}")
mylist[1:2] = ["d", "e"]  # "d" replaces "b" while "e" doesn't replace anything but pushes in front of "c" instead
print(f"by slicing characters again we can replace 'b' but not 'e'?! ----> {mylist}")

# Putting in less than taking will put the new items where specified making the current items move accordingly
mylist[1:3] = ["f"]  # changes the 2nd and 3rd value with "f"
print(f"by slicing characters once more we can this time replace the 2nd value"
      f"but the 3rd is safe?! ----> {mylist}")

########################################## Functions ##################################################################
print(f"\n{'List Functions':#^65}")
"""
Used to add to the list without replacing any of the current values. Using extend() you can add any iterable object. 
Again tuples and sets don't allow to do this. Appending something lets you add it but purely at the end of the list,
len is the length of the list, inserting is pretty much appending except you can place it anywhere
"""

l, w, idx = [1, 2, 3, 4, ], ['learning', 'coding'], 0
# l.append(4), w.insert(idx, 'I am'), l.count(4), l.reverse(), l.remove(4)

print(f"Adding '4' to the list 'l' by using '.append()' ----> {l}\nFinding how long the list is by using "
      f"'len' ----> {len(l)}\nAdding another item 'numbers' to the list using '.insert()' ----> "
      f"{w.insert(idx, 'I am')}\nLets find the highest number in 'l' by using 'max' ----> {max(l)}\nNow we have the "
      f"largest number, there is more than 1 of it....there are ----> {l.count(4)}\nLike things backwards? lets do "
      f"that with '.reverse()' ----> {l.reverse()}\nLastly we only want 1 of the max number so lets remove 1 using "
      f"'.remove()' ----> {l.remove(4)}")

########################################### Sorting and Copying ######################################################
print(f"\n{'Sorting and Copying':#^65}")
"""
Organises the list alphabetically or numerically, ascending or descending, you can even customise how you sort it.
Tuples have a default order that can't be changed while a set has no order at all making it impossible to know what 
order the output will be in.
"""

o, s, sn = ["grape", "orange", "seeds", "apple"], ["grape", "Orange", "seeds", "Apple"], [1, 10, 100, 20, 3]
s.sort(), sn.sort(), s.sort(reverse=True), sn.sort(reverse=True), s.reverse(), sn.reverse(), s.sort(key=str.lower)
print(f"the original lists ----> {o} and {sn}\nWe will sort them in ascending order using '.sort()' ----> "
      f"{s} and {sn}.\nNow that we sorted them, let's do it in reverse! using '.sort(reverse=True)' ----> "
      f"{s} and {sn}.\nWithout sorting we can simply reverse the order making it start from 'Apple' and '3' "
      f"using '.reverse()' ----> {s} and {sn}.\nAt last we have the ability to make out 's' list case-sensitive"
      f"using .sort(key=str.lower) ----> {s}\n")


def my_sort(d):
    return abs(d - 20)  # specifies "20" to be the key argument making it 1st before just printing the list regularly


sn.sort(key=my_sort)
print(f"Using the 'absolute' function or 'abs' we can target '20' within our list moving it to the front ----> {sn}")

"""
To copy a list you can't simply just copy the same list as any changes made will affect both lists, you can do this
by using copy() or list(), a tuple can't be made copies of.
"""

sl, sr = {1, 2, 3, 4}, ["Hello", "There"]

print(f"To get another list or set without making changes to the original you have to use '.copy()' to"
      f"create a copy of it ----> {sr.copy()} and {sl.copy()}")

#######################################################################################################################
#                                                          LOOPS                                                      #
#######################################################################################################################
"""
A loop will run in a repeated circle until the correct answer is given, without running the program repeatedly.
For this to work, everything has to be within the "while" statement otherwise it won't be looped. The change of
"counting" from True to False lets the loop continue to the else statement, otherwise will repeat the loop even if
the correct answer is given.
"""

#######################################################################################################################
#                                                     WHILE LOOP                                                      #
#######################################################################################################################
print(f"\n{'The While Loop - 1st Example':#^65}")
"""Executes a set of statements as long as the condition is True"""

number, numbers, num = 1, 0, 1

while number < 20:  # will loop through until it hits "20" printing the results it found from "number"
    print(f"Looping until '20' ----> {number}")
    # The break statement #
    """Lets you stop a loop regardless of a True condition, used for the 'for loop' as well"""
    if number == 20:
        break  # stops the loop once the loop reaches "19"
    number += 1
print(f"\n{'The While Loop - 2nd Example':#^65}")
while numbers < 6:
    numbers += 1
    # The continue statement #
    """stops the current iteration and continues to the next, used for the 'for loop' as well"""
    if numbers == 3:
        continue  # once "3" is hit, skips it and goes to "4"
    print(f"This while loop will skip '3' how cool is that! ----> {numbers}")
print(f"\n{'The While Loop - 3rd Example':#^65}")
while num < 6:
    print(f"This loop will stop at '5' ----> {num}")
    num += 1

############################################## Looping Lists, Tuples and Sets #########################################
print(f"\n{'Looping Lists, Tuples and Sets':#^65}")
mylist, i = ["Hello", "There", "Buddy"], 0

while i < len(mylist):  # loops through 'i' comparing it to the length of mylist
    print(f"We did loops through while looping so now let's do it through lists! ----> {mylist}")
    i += 1  # adds 1 to i until it is no longer lesser length than my list

#######################################################################################################################
#                                                       FOR LOOP                                                      #
#######################################################################################################################
print(f"\n{'The For Loop':#^65}")
"""Executes a set of statements, once per item in a list, tuple, set, etc."""

items = ["apple", "bread", "snacks"]
print(f"Simply what we are doing here is printing the items found within the list 'items' ----> {[x for x in items]}")

###############################################  Looping Through a String #############################################
print(f"\n{'Looping Through a String':#^65}")
print(f"Suck at counting letter? just spell it out 1 at a time ^^ ----> {[x for x in 'apple']}")

###############################################  The range() function #################################################
print(f"\n{'The Range() Function':#^65}")
"""Returns a list of numbers from 0 going by increments of 1, stopping at a specific number"""

print(f"Using 'range()' we will get total '6' number starting from '0' ----> {[x for x in range(6)]}")
print(f"Now we will be a little more specific with our numbers ----> {[x for x in range(2, 6)]}")
print(f"After being specific what can we do?...let's try increasing the value by '3'"
      f"instead of the default '1' ----> {[x for x in range(2, 30, 3)]}")

x = int(input('Please enter a number: '))
print(f"The list of numbers multiplied by 3 and 5 are ----> {[i for i in range(x) if i % 3 and i % 5 == 0]}")

###############################################  Nested Loops #########################################################
print(f"\n{'Nested For Loops':#^65}")
"""Simply just a loop within a loop with the inner loop being executed 1 time for each iteration of the outer loop"""

color, items = ["red", "blue", "yellow"], ["apple", "ball", "shirt"]

for x in items:
    for y in color:
        print(f"We are almost done with loops, so it's time to try looping through multiple lists! ----> {y, x}")

############################################### The pass statement ####################################################
print(f"\n{'The Pass Statement':#^65}")
"""Prevents an error being raised if there is an empty space within the loop"""

# it isn't shown but at the end of the if statement under the : part just write pass, and it will have the same effect
print(f"Using the 'pass' statement to finish loops sounds like a good idea! ----> {[x for x in [1, 2, 3]]}")

#######################################################################################################################
#                                               EXERCISE                                                              #
#######################################################################################################################
print(f"\n{'Exercise Practice: Removing All Even Numbers':#^65}")
n = int(input('Please put your numbered choice here: '))

for i in range(1, n, 2):
    if i % 3 == 0 and i % 5 == 0: print(f"Learning Python")
    elif i % 3 == 0: print(f"Learning")
    elif i % 3 == 0: print(f"Python")
    else: print(f"{i}")