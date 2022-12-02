"""
This file contains in the following order:
1. Commenting and Printing:
      Commenting Out Code
      Printing the Output
2. Math:
      General
      Int, Float and Complex
      Type conversion
      Using Import Math
3. General Operations:
      Assignment
      Bitwise or Binary
4. Exercise
"""

#######################################################################################################################
#                                        COMMENTING AND PRINTING                                                      #
#######################################################################################################################

######################################### Commenting Out Code #########################################################
# <---- This is a single line comment, you can use it above, under or next to a line of code, also prevents running code
"""
This is using something called multi-line comments which unlike the # comment this lets you use multiple lines, however
it doesn't wrap itself, so you have to make it look clean yourself. This is an excellent way of explaining things in
great detail, as being done in this example.

Using both comment styles within the code will make the code look more details and much easier to read.
"""

######################################### Printing the Output #########################################################
print(f"{'Printing the Output':#^65}")
"""Print() is a function that tells the computer what to write or do.The information between "" is a String which is
bunch of characters or text.
"""
print("Hello World!")

"""
When dealing with printing out strings with multiple values or variables you can use the formatted string literal
known as f-string to do it cleanly and quickly. To do this you put an 'f' after the first bracket, this way you won't
need to use the full sentence or method of format as it will format the string automatically. This is HIGHLY
recommended when printing as it lets you avoid pointless variables and methods.
"""
print(f"Strings and variables go here")

#######################################################################################################################
#                                                MATH                                                              #
#######################################################################################################################
"""
Using C standard code behind the scenes this lets you access math functions that can't be used for more complex things
but for the most part general to advanced math, to use complex math functions you would need to use the module cmath.
Getting an exception instead of results that may be confusing lets you know what the complex number was and why it was
created.

Python follows the traditional operations making it:
1st: parentheses ()
2nd: exponentiation **
3rd: multiplication/division * /
4th: addition/subtraction + -
"""

################################################ General ##############################################################
print(f"\n{'General Math':#^65}")
"""Used mainly when using math"""
addition = 2 + 2
print(f"simple addition ----> {addition}")

subtraction = 3 - 1
print(f"simple subtraction ----> {subtraction}")

multiply = 2 * 2
print(f"simple multiplication ----> {multiply}")

power = 2 ** 5
print(f"basic powering or squaring of a number ----> {power}")

division = 4 / 2
print(f"simple division ----> {division}")

rounding = 20 // 5
print(f"simply dividing and rounding the numbers ----> {rounding}")

remainder = 12.5 % 5
print(f"calculates the amount of times 5 goes into 12.5 and returns what is left ----> {remainder}")

########################################## Int, Float and Complex #####################################################
print(f"\n{'Int, Float and Complex':#^65}")
"""A whole number regardless if positive or negative"""
a, b, c = 1, 123456, -12
print(f"{type(a), a}\n{type(b), b}\n{type(c), c}")

"""A number that used one or more decimal points regardless of positive or negative, can also use "e" for power of 10"""
a, b, c, d = 1.1, 1.2, -1.3, 10e4
print(f"{type(a), a}\n{type(b), b}\n{type(c), c}\n{type(d), d}")

"""Visually represented as a couple of numbers that uses real and fake numbers to form a vector"""
a, b, c = 3 + 5j, 5j, -5j  # "j" is the fake or imaginary number
print(f"{type(a), a}\n{type(b), b}\n{type(c), c}")

########################################## Type Conversion ############################################################
print(f"\n{'Type Conversion':#^65}")
"""Used to change a value from one number method to another"""
a, b, c = 1, 1.2, 1j

"""a changes to float, b to int and a again to complex"""
a, b, c = float(a), int(b), complex(a)
print(f"{type(a), a}\n{type(b), b}\n{type(c), c}")

########################################### Using Import Math #########################################################
print(f"\n{'Calculating with Import Math':#^65}")
import math
x, y = (23, -88), (6, 42)

print(f"The distance between the coordinates is ----> {math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))}")

#######################################################################################################################
#                                                GENERAL OPERATORS                                                    #
#######################################################################################################################
"""
Operators are very useful and most of the time very important in making the code not just clean and efficient but
also very powerful. Below are a list of various operators with their functions and examples.
"""

########################################### Assignment ################################################################
print(f"\n{'Assigning Values to Variables':#^65}")
"""Used to assign values to variables"""
x = 5
print(f"'x = 5' is the same as 'x = 5' ----> {x}")
print(f"'x += 5' is the same as 'x = x + 5' ----> {x + 5}")
print(f"'x -= 5' is the same as 'x = x - 5' ----> {x - 5}")
print(f"'x *= 5' is the same as 'x = x * 5' ----> {x * 5}")
print(f"'x /= 5' is the same as 'x = x / 5' ----> {x / 5}")
print(f"'x %= 5' is the same as 'x = x % 5' ----> {x % 5}")
print(f"'x //= 5' is the same as 'x = x // 5' ----> {x // 5}")
print(f"'x **= 5' is the same as 'x = x ** 5' ----> {x ** 5}")
print(f"'x &= 5' is the same as 'x = x & 5' ----> {x & 5}")
print(f"'x |= 5' is the same as 'x = x | 5' ----> {x | 5}")
print(f"'x ^= 5' is the same as 'x = x ^ 5' ----> {x ^ 5}")
print(f"'x <<= 5' is the same as 'x = x << 5' ----> {x << 5}")
print(f"'x >>= 5' is the same as 'x = x >> 5' ----> {x >> 5}")

########################################### Bitwise or Binary #########################################################
print(f"\n{'Basic Bitwise or Binary':#^65}")
"""Used to compare binary numbers"""
lshifts = 2 << 2  # 2 is 10 in bits, shifting by 2 bits gives 1000 which is "8" in decimal
print(f"lets push some '0s' from the right, letting leftmost bits fall off! ----> {lshifts}")

rshifts = 11 >> 1  # 11 is 1011 which is 101 when shifted to the right by 1 making it a decimal of 5
print(f"lets push copies of the leftmost bit in from the left, letting the rightmost bits fall off! ----> {rshifts}")

and_bits = 5 & 3  # 0101 & 0011 give 0001
print(f"if both bits are '1' we should set the bit to ----> {and_bits}")

or_bits = 5 | 3  # 0101 | 0011 gives 0111
print(f"if either bits are '1' we should set the bit to ----> {or_bits}")

xor_bits = 5 ^ 3  # 0101 ^ 0011 gives 0110
print(f"if both bits are the same we should set the bit to '0' otherwise set it to  ----> {xor_bits}")

# inverts all the bits
not_bits = ~ 5
print(f"i think it's time we invert all the bits :D ----> {not_bits}")

#######################################################################################################################
#                                               EXERCISE                                                              #
#######################################################################################################################
print(f"\n{'Exercise Practice: Calculating a Total':#^65}")

interest, invested, invest = 0.01, 100, 0.01 * (2 ** 20)

print(f"Using ** calculate the total interest returned from an investment if it was doubled daily for 20 days and "
      f"choose either to wait for the return of interest or walk with the current amount:\nThe investment was "
      f"${invested:.2f}, if we wait 60 days our interest would be ${invest:.2f}")
