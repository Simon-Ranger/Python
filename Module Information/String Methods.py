#######################################################################################################################
#                                                 STRING METHODS                                                      #
#######################################################################################################################
"""The original strings aren't affect by the returned new value of the string method."""

########################################### Changing Case Structure ###################################################
cap = "capitalize()"  # makes the 1st character upper case
Title = "title()"  # makes the 1st character of each word upper case
high = "upper()"  # makes the string into upper case
case, low = "casefold()", "lower()"  # makes the string into lower case
swapcase = "swapcase()"  # swaps lower to upper case and vice versa

########################################### Changing tab spaces #######################################################
expand = "expandtabs()"  # sets the tab size for the string

########################################### Finding a Value ###########################################################
find, index = "find()", "index()"  # looks for a specified value, letting you know where it was found
join = "join()"  # joins elements of an iterable to the end of a string (ex. sequence types)
rfind, rindex = "rfind()", "rindex()"  # looks for a specified value, letting you know the last place it was found
split, rsplit = "split()", "rsplit()"  # Splits the string at a specified separator returning a list

########################################### Formatting ################################################################
form, format_map = "format()", "format_map()"  # formats specified values to a string

########################################### Filling and Splitting a String ############################################
splitlines = "splitlines()"  # splits the string at line breaks returning a list
zfill = "zfill()"   # fills the string with a specified amount of 0 values at the start

#######################################################################################################################
#                                            RETURNING STRING METHODS                                                 #
#######################################################################################################################

########################################### Returning Numbers and Letters as Characters ###############################
allnum = "isalnum()"  # returns True if the string contains only number characters
allaph = "isalpha()"  # returns True if the string contains only alphabetical characters
isdec = "isdecimal()"  # returns True if the string contains only decimals
lower = "islower()"  # returns True if the string contains only lower case characters
higher = "isupper()"  # returns True if the string contains only upper case characters
num = "isnumeric()"  # returns True if the string contains only numeric characters

########################################### Returning an Identifier and Printable #####################################
identifier = "isidentifier()"  # returns True if the string is an identifier
printable = "isprintable()"  # returns True if the string is characters are printable

########################################### Returning Trimmed Strings #################################################
strip = "strip()"  # returns a trimmed version of the string
lstrip = "lstrip()"  # returns a left trim version of the string
rstrip = "rstrip()"  # returns a right trim version of the string

########################################### Returning True ############################################################
space = "isspace()"  # returns True if the string contains only whitespace characters
title = "istitle()"  # returns True if the string follows the rules of a title
startswith = "startswith()"  # returns True if the string starts with a specified value
endswith = "endswith()"  # returns True if the string ends with a specified value

########################################### Centering a String ########################################################
center = "center()"  # returns a centered string

########################################### Parting and Replacing a String ############################################
partition = "partition()"  # returns a tuple with the string parted into 3 parts
replace = "replace()"  # returns a string where the value has been changed with another specified value

########################################### Justifying, Counting and Encoding a String ################################
just = "!just()"  # returns a left justified version of the string
count = "count()"  # returns how often a specified value is used in a string
encode = "encode()"  # returns an encoded version of the string

########################################### Translating a String ######################################################
make = "maketrans()"  # returns a translation table to be used in translations


