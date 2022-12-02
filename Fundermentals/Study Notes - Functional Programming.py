"""
This file contains in the following order:
1. Lambda:
    General Use
    Functional Use
2. Map & Filler
3. Generators & Decorators
4. Itertools
5. Exercise
"""

#######################################################################################################################
#                                                   LAMBDA                                                            #
#######################################################################################################################
"""
A small anonymous function that can take any number of arguments but only one expression, best to be used when
wanting to hide it within another function that might take one argument which needs to be multiplied with an unknown
number.
"""

############################################### General Use ###########################################################
print(f"\n{'General Lambda Use':#^65}")
"""The expression is executed returning the result"""
a = lambda x: x + 15
print(f"Using the 'Lambda' function we can make 'x' become '10' making 'x + 15' become ----> {a(10)}")
a = lambda b, c: b * c
print(f"With this example we will multiply '10' or 'b' by '5' or 'c' to get ----> {a(10, 5)}")

a = lambda e, d, f: e + d + f
print(f"Time to try adding multiple values together! '5' or 'e' + '10' or 'd' + '12' or 'f' to get ----> "
      f"{a(5, 10, 12)}")  # "e=5, 10=d, f=12" which is all added together

x = int(input('Please enter a number: '))
y = (lambda z: z ** 3)(x)
print(f"The cubed result of your number is ----> {y}")

names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
print(list(filter(lambda x: len(x) > 5, names)))

################################################ Functional Use #######################################################
print(f"\n{'Functional Lambda Use':#^65}")


def lamdba_fuct(a):
    return lambda h: h * a


double = lamdba_fuct(5)  # the multiplier which can be changed easier to suit the amount you need
print(f"Lets make it easier to change the amount being multiplied by using the functional use of 'lambda' "
      f" multiplying '10' or 'h' by '5' or 'a' ----> {double(10)}")

#######################################################################################################################
#                                                  MAP and FILTER                                                     #
#######################################################################################################################
print(f"\n{'Mapping and Filtering':#^65}")
"""
These built-in functions are highly powerful when operating lists, the 'map' function takes a function with an
iterable as arguments, returns a new iterable applying the function to each argument, converting the result into a list
would require the 'list' function. The 'filter' function removes any items within the list that doesn't match a
function that returns a boolean These are even more powerful when mixed with other functions such as lambda.
"""

names, nums = ["David", "John", "Annabelle", "Johnathan", "Veronica"], [11, 20, 43]
print(f"{list(map(lambda x: x * 2, nums))}")
print(f"{list(filter(lambda x: len(x) > 5, names))}")

#######################################################################################################################
#                                                  GENERATORS and DECORATORS                                          #
#######################################################################################################################
print(f"\n{'Generators and Decorators':#^65}")
"""
Generators are similar to lists but don't allow you to index them, but can still be used in loops, to create them you use
functions with the 'yield' statement that defines a generator replacing the return function, providing a result without
destroying any of the local variables.

Decorators modify functions by using other functions which comes in handy when wanting to extend the use of a function
without having to actually modify it. If you want to decorate the function use an '@' above it with whatever name you
want the decor to be, a single function can have multiple decors
"""

# Generator
txt = input('Please enter some text: ')


def words(txt):
    for word in txt.split(' '):
        yield word


print(f"This is a breakdown list of the word(s) in your sentence {list(words(txt))} <---- a generator")

# Decorators
text = input('Warning...text will become all upper case, please enter a word or sentence: ')


def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()

    return wrapper


@uppercase_decorator
def display_text(text):
    return text


print(f"{display_text(text)} <---- a decorator")

#######################################################################################################################
#                                                        ITERTOOLS                                                    #
#######################################################################################################################
print(f"\n{'The Power of Itertools':#^65}")
"""
This is a module built-in to python containing multiple very useful and powerful functions as they work similar to map
or filter making the code run a lot smoother while making it also maintain a very clean look!. Some of these are:

'count' which counts up infinity from a value, 'cycle' which does the same as count but with lists and strings instead
of a value, 'repeat' speaks for itself repeating an object infinitely if not specified otherwise. There is also others
like 'takewhile' which takes items from an loop as long as the boolean is true (does the same thing as a while loop but
without the code), 'chain' simply joins multiple loops in to 1 and 'accumulate' which returns the total of values in
a loop.

Other great functions within itertools are 'product' and 'permutation' used when wanting all possible combinations
within a list of items.
"""

print(f"\n{'count':#^10}")
from itertools import count, cycle, repeat, chain, accumulate, takewhile, product, permutations

for i in count(3):
    print(f"counting up from': {i}")
    if i >= 11:
        break

print(f"\n{'cycle':#^10}")
c = 0
ts = input('This will breakdown the word until the specified number is hit....Please enter a word: ')

for i in cycle(ts):
    print(f"{i}")
    c += 1
    if c > 5:
        break

print(f"\n{'repeat':#^10}")
c = 0
ts = input('This will repeat what you say a specific amount of times....Please enter a word: ')

for i in repeat(ts):
    print(f"{i}")
    c += 1
    if c >= 3:
        break

print(f"\n{'takewhile and accumulate':#^10}")
nums = list(accumulate(range(8)))
print(f"{nums}\n{list(takewhile(lambda x: x <= 6, nums))}")

print(f"\n{'chain':#^10}")
print(f"{list(chain([1, 2, 3], ['one', 'two', 'three'], 'string'))}")

print(f"\n{'product and permutations':#^65}")
letters = ("A", "B")
print(f"{list(product(letters, range(2)))}\n{list(permutations(letters))}")

#######################################################################################################################
#                                                        EXERCISE                                                     #
#######################################################################################################################
print(f"\n{'Exercise Practice: Fibonacci Using Recursive':#^65}")
num, fib = int(input('Please enter a number: ')), [0, 1]


def fibs(n):
    if n == 2: print(f"{[i for i in fib]}")
    else: fib.append(sum(fib[-2:])), fibs(n - 1)


print(f"{fibs(num)}")
