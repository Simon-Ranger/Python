#######################################################################################################################
#                                                   Files                                                             #
#######################################################################################################################
"""
Making code that can interact with the user is where the most fun of coding can come from, it also is used in most
proper apps people use around the world without understanding that someone made that happen using code. It can also
be very useful when dealing with files.
"""

########################################### Palindrome#################################################################
print(f"\n{'Determining Palindrome':#^65}")


def backwards(text):
    return text[::-1]


def is_palindrome(text):
    return text == backwards(text)


# If the text and reverse text are the same it's a palindrome
typing = input("Type your message here: ")
if is_palindrome(typing):
    print(f"The text can be reversed making it a palindrome")
else:
    print(f"The text can't be reversed making it a palindrome")

########################################### Working with Files ########################################################
"""
When it comes to files using python you can not just open, but read, write and close a file using various methods.
This comes in very handy when wanting to use python for data collection or simply just help keep things organised.
"""

print(f"\n{'Creating & Opening Files':#^65}")
"""
You can use + with the letters to give additional permissions turning 'r' read only to 'r+' read and write. To simply
just read a file specifying the file is enough, you won't need any letters after it.
"""

f = open("testing.txt", "w")  # the 'w' is for writing in to a text file
nf = open("newfile.txt", "x")  # creates a new empty file, will show an error if already exists
"""
open("testing.txt", "r")    # the 'r' is for purely reading the file
open("testing.txt", "t")    # this is similar to 'r' where it opens the file in text mode
open("testing.txt", "b")   # the 'b' is for non-text based files (binary, including images and sounds)
"""

print(f"\n{'Writing to Files':#^65}")
nf.write("WOW...we just created a new file!")

f.write("""
I really love python,
it's fun to play around with.
Lets learn together!
""")

print(f"\n{'Reading Files':#^65}")
"""
If the file is not directly in the same location as the script it won't work unless you put in the location of it when
opening the file. You can also read specific things from a file including how many characters by adding a number in ()
or using 'readline' to read a single line or simply loop through the file to get the data you want.
"""
f, nf = open("testing.txt"), open("newfile.txt")
print(f"We are reading text from 'testing.txt' is:{(f.read())}")
print(f"We are reading the data from 'newline.txt':\n{nf.read()}")

for line in f:
    print(line)

print(f"\n{'Closing Files':#^65}")
"""
Sometimes a file won't accept the changes made to it without it being closed first, it is also important to close the
file when finished to prevent buffering.
"""

print(f"Closing Files....", f.close(), nf.close())

print(f"\n{'Deleting Files':#^65}")
"""
When needing to delete files or directories you need to import the os module first otherwise it won't work. You can
also set up checks to prevent errors before deleting the file.
"""
import os

os.remove("newfile.txt")  # removes the file 'newfile.txt'

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")  # checks if the file exists
else:
    print(f"The file does not exist")

# os.rmdir("Random")  # deletes the whole file, must be empty to be deleted

"""
To make all the other try blocks cleaner using a "with" statement is perfect as it enables you to do such a thing. With
gathers the object from the open statement calling xfile.__enter__ before starting and xfile.__exit__ before finishing
the block of code. Using this lets you not have to use try...except repeatedly 
"""

########################################### Using Imports to Save Data ################################################
print(f"\n{'Using Pickles to Save Data':#^65}")
"""
When things get too messy you could lose track of where things are, using a module called "Pickle" you can prevent this
by placing any plain python object into a file for later use.
"""

import pickle  # imports the module pickle from the python library

foodlistfile = "foodlist.data"  # naming the file storing the objects
foodlist = ["fruits", "beef", "snacks"]  # basic string showing what items/objects are needed

f = open(foodlistfile, "wb")  # writes the items into the file
pickle.dump(foodlist, f)  # dumps the items into a file
f.close()

del foodlist  # deletes the original variable "foodlist"

f = open(foodlistfile, "rb")  # reads from the stored file we originally created
storedlist = pickle.load(f)  # simply loads the stored file
print(f"The list of food was: {storedlist}")
f.close()

########################################### Reading Foreign Characters ################################################
print(f"\n{'Using Import io to Read Foreign Characters':#^65}")
"""
For those that might not use English characters a thing in python is called "unicoding" which represents both english
non-english characters.
"""

# encoding=utf-8 (must be at the very top of the file to tell python we will be using this encoding type).
import io  # imports the module needed for dealing with pythons main facilities relating to input/output.

f = io.open("hello.txt", "wt", encoding="utf-8")  # encodes the message
f.write(u"안녕하세요")  # the "u" enforces python to understand that the program using UTF-8 encoding
f.close()

text = io.open("hello.txt", encoding="utf-8").read()  # decodes the message
print(f"{text}")

############################################ Analyzing The Text Once Opened ###########################################
print(f"\n{'Analyzing Text Data':#^65}")


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


file = open("random.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")

file.close()
filename = "random.txt"

with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
