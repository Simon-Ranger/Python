"""
This file contains in the following order:
1. Exceptions:
    Types of Exceptions
    Try and Except
    File Exceptions
2. Exercise
"""

#######################################################################################################################
#                                                   EXCEPTIONS                                                        #
#######################################################################################################################
"""
Even codes can be wrong or something can happen you didn't expect, however you can also code things to help check,
prevent and even handle those situations. Normally when programming it will give an error type of the mistake that was
made.
"""

######################################### Types of Exceptions #########################################################
print(f"\n{'Exception Types':#^65}")
"""
There are countless of exception errors since a lot of 3rd party libraries have their own + python having some in-built
ones of their own. Pythons built-in exceptions are:
"""

print(f"{'Exception Tree':#^45}")
print("""BaseException:
        SystemExit
        KeyboardInterrupt
        GeneratorExit
        Exception:
            StopIteration
            StopAsyncIteration
            ArithmeticError:
                FloatingPointError
                OverflowError
                ZeroDivisionError
        AssertionError
        AttributeError
        BufferError
        EOFError
        ImportError:
            ModuleNotFoundError
        LookupError:
            IndexError
            KeyError
        MemoryError
        NameError:
            UnboundLocalError
        OSError:
            BlockingIOError
            ChildProcessError
            ConnectionError:
                BrokenPipeError
                ConnectionAbortedError
                ConnectionRefusedError
                ConnectionResetError
            FileExistsError
            FileNotFoundError
            InterruptedError
            IsADirectoryError
            NotADirectoryError
            PermissionError
            ProcessLookupError
            TimeoutError
        ReferenceError
        RuntimeError:
            NotImplementedError
            RecursionError
        SyntaxError:
            IndentationError:
                TabError
        SystemError
        TypeError
        ValueError:
            UnicodeError:
                UnicodeDecodeError
                UnicodeEncodeError
                UnicodeTranslateError
        Warning:
            DeprecationWarning
            PendingDeprecationWarning
            RuntimeWarning
            SyntaxWarning
            UserWarning
            FutureWarning
            ImportWarning
            UnicodeWarning
            BytesWarning
            ResourceWarning
""")

########################################## Try and Except #############################################################
print(f"{'Using Try and Except':#^65}")
"""
Using something called the try-except statement you can handle exceptions or errors such as the one shown below. The
input when using "ctrl-d" or anything that interrupts the regular way of things will display the printed messages.
"""

try:  # puts everything that might cause issues into this block to try to run through each once executing the code.
    words = input("This should work right? ")
except EOFError:  # handles any end of file errors
    print("Ah still didn't work?!?")
except KeyboardInterrupt:  # handles anything mistyped by the keyboard
    print("I'm out to learn more!")
else:
    print(f"Yay you got to enter {words}")  # prints whatever you typed

"""
With exceptions as long it's part of the exception class you can raise or call an exception by providing the error type 
being thrown.
"""


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    message = input("Message goes here --> ")
    if len(message) < 5:
        raise ShortInputException(len(message), 5)
except EOFError:
    print(f"why's this happening!")
except ShortInputException as ex:
    print(f"ShortInputException Error: The message had {ex.length} characters long, expected {ex.atleast} or more")
else:
    print(f"No issues found!")

# Makes it so the input is purely numbers otherwise raises an error
pin = input('Please enter the PIN you want to use: ')
try:
    int(pin)
    print(f"Your PIN has been created")
except ValueError:
    input(f"Please try again using numbers only: ")
    print(f"Your new PIN is {pin}")

########################################### File Exceptions ###########################################################
print(f"\n{'File Exceptions':#^65}")
"""
sometimes the file might not close properly even with exceptions raised to prevent it, to make sure the file is closed
use the "finally" command. Finally defines a block of code when "try...except" is final, this will run regardless of 
errors. Used mainly to close objects and clean resources.
"""

import sys  # provides functions and variables used to manipulate various parts of the python runtime environment.
import time  # imports all the related time modules

f = None

try:
    f = open("statement.txt")  # opens the file
    while True:
        line = f.readline()  # reads the file
        if len(line) == 0:
            break
        print(f"{line}", end="")
        sys.stdout.flush()  # forces the program to buffer all data to the terminal without waiting
        print(f"Press ctrl+c now")
        time.sleep(2)  # forces the code to sleep for the allocated time period making it run a lot slower than normal.
except EOFError:
    print(f"couldn't find file!")
except KeyboardInterrupt:
    print(f"Cancelled file reading")
finally:
    if f:
        f.close()
    print(f"closing file!")

#######################################################################################################################
#                                                     EXERCISE                                                        #
#######################################################################################################################
print(f"\n{'Exercise Practice: Reading Data from a Text File':#^65}")

file = open("statement.txt", "r")
s = file.readlines()
for i in s:
    i = i.replace("\n", "")
    print(i[:1] + str(len(i)))
file.close()
