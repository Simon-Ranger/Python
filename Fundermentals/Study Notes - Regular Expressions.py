"""
This file contains in the following order:
1. Regular Expressions:
    Using Re:
        Compiling
        Backslash Plague
        Performing
        Module Level Functions
        Compilation Flags
2. Functions
3. Matching Objects:
    re.Match
    re.Search
    Search and Replace
    Repeating
4. Metacharacters
5. Characters
6. Groups:
    Non-capturing and Named Groups
    Lookahead Assertions
7. Special Sequences
8. Email Extraction
9. Exercise
"""

#######################################################################################################################
#                                                    REGULAR EXPRESSIONS                                              #
#######################################################################################################################
"""
Regular Expressions (regex or RE) are tiny, highly special form of programming language mixed in with python and can be
used via the 're' module. When using it you specify the set of strings you want to search or match, ranging from
general text to emails or forms of commands, you can also use this to split or modify a string in various ways.

This language is compiled by a series of bytecodes that are executed by a matching script writen in C language. If
wanting to use it for more advanced purposes it'll be best to pay close attention to how the engine executes a given
RE, writing it a specific way to make it run faster.

You can't use RE for all possible string processing, depending on the situation it could be better to just write
normal python code. To turn a regular string in to a "raw string" to help work with REs easier is simply putting 'r'
in front of the string.
"""

#######################################################################################################################
#                                                       USING RE                                                      #
#######################################################################################################################
"""
To use RE in python you need to import the 're' module which provides an interface to the RE engine allowing it to
compile into objects then perform matches using them.
"""

print(f"\n{'Importing RE':#^65}")

import re

print(f"Importing re...")

################################################### Compiling #########################################################
print(f"\n{'Compiling a RE':#^65}")
print(f"{'Compiling':#^67}")
"""
These are compiled into pattern objects having methods for multiple operations including searching for patterns or 
performing string substitutions.
"""

import re

c = re.compile('ab*')
print(f"Using '.compile()' parse the RE as a string ----> {c}")

#################################################### Backslash Plague #################################################
"""
Since python uses the backslash for general purposes it conflicts with the RE usage of it, so you have to put a single
backslash for RE usage, double backslash for re.compile() usage and a total of 4 backslashes for it to be escaped and
used as a string literal. If the RE being used consists of a lot of backslashes it will make strings look messy and
hard to read, to get around this issue and make the code look clean and readable put an 'r' character which means it 
will become a raw string using the 'raw string notation'.
"""

###########################################
#     Regular String    #     Raw String  #
###########################################
#      "ab*"            #    r"ab*"       #
###########################################
#      "\\\\section"    #    r"\\section" #
###########################################
#      "\\w+\\s+\\1"    #    r"\w+\s+\1"  #
###########################################

##################################################### Performing ######################################################
print(f"\n{'Performing a RE':#^65}")
"""
The 4 main methods used with RE are '.match()', '.search()', '.findall()' and '.finditer()' which will be explained
more within the 'RE module' file. After matching data you can query it the objects for even greater information by using
querying methods '.group()', '.start()', '.end()' and '.span()' which are the most important ones currently used.
Unlike matching, .search() might not start at '0' as it scans through the string.
"""

c = re.compile('[a-z]+')
p = c.match('tempo')

# Relating to .match() and .search()
print(f"This will compile the RE that will be used for the other method tests ----> {c}\nSince '+' is being used an "
      f"empty space should be matched returning ----> {c.match('')}\nIf something matches the output will tell you"
      f"what the match was as well as other information regarding the match ----> {p}\nThe '.group()' method simply "
      f"returns what was matched by RE ----> {p.group()}\nUsing '.start()' simply returns the starting position of "
      f"the match ----> {p.start()}, while '.end()' returns the last position ----> {p.end()}\nbut are returned as "
      f"indexed numbers rather than 't' and 'o'\nIf you want to return both start and end using '.span()' is the "
      f"option to go with ----> {p.span()}\nLets search for something now! ----> {c.search(':::: message')}\n")

"""
When RE is used in actual codes it normally is within an if statement, and uses the '.findall()' and '.finditer()'
methods to return a list of matching strings or the sequence of matching instances as an interator.
"""

# Relating to .findall() and .finditer()
it = c.finditer('this is very interesting and i am really enjoying it')

print(f"This should find all the matching strings and return it as a list ----> "
      f"{c.findall('this is very interesting and i am really enjoying it')}\nThis should give the iterator ----> "
      f"{it}\nUsing a for loop you can see the span of the string by using both .span() and .finditer() together as "
      f"shown below:\n")

for match in it: print(f"Counting the index of each character of the string ----> {match.span()}")

###################################################### Module Level Functions #########################################
print(f"\n{'Module Level Functions':#^65}")
"""
We have gone over .match(), .search() and .findall() but there is another called '.sub()', which returns a string with
all matching occurrences of the pattern are replaced by the replace string these functions generally create and call
the needed method as well as work as a storage for cache regarding objects that have been complied, letting future
calls won't repeatedly get passed through the same RE. When to use these would be within loops as it saves time with
function calls, but outside of loops doesn't make much difference.
"""

print(f"Lets try to replace letters within a string using .sub() ----> "
      f"{re.sub('[a,I]', 'b', 'Can we change the letters in this string')} <---- "
      f"haha funny, all 'a' characters are now 'b'")

####################################################### Compilation Flags #############################################
print(f"\n{'Complication Flags':#^65}")
"""
These let you modify certain aspects of RE, they have 2 names within the re module being a long self 'IGNORECASE' and 
a short self such as 'I'.
"""

# IGNORECASE, I
"""
Matches case sensitive character classes and literal strings simply by ignoring the cases used [A-Z] will look for both
upper and lower case instead of purely uppercase, the easiest way to use this is to parse it through another RE
function.
"""

print(f"This will ignore all the case sensitive characters ----> {c.match('Hopefully this Works!', re.I)}")

# LOCAL, L
"""
If you don't want to use the unicode database, using this will make '\\w, \\W, \\b and \\B' as well as case sensitive
rely on local instead. These are C library features designed to help with coding related to various spoken languages,
which is very useful when needing to match bytes to characters with accents on them 'é' for example. However using this
in python 3 is HIGHLY NOT recommended as its not very stable and overall unicode is a generally better option.
"""

l = re.compile('[\w+a-z]')
txt = l.search('수업 전 또는 선행의')
print(f"{txt, re.L}")

# MULTILINE, M
"""
This simply if specified this applies to every line after a new line has been formed, meaning that ^ will match the
beginning of the string of each new line, while $ does the same but at the end of the string.
"""

m = re.compile('[^\w{3}]')
new = m.search('Hello\nhow are you')
print(f"The match should be a new line! ----> {new, re.M}")

# DOTALL, S
"""
Simply makes '.' match any character including new lines, without it will match everything but a new line.
"""
text = 'Hello\nthere'
print(f"This won't have a new line ----> {re.search(r'.+', text)}\nwhile this will include the new line since we used"
      f"'re.S' ----> {re.search(r'.+', text, re.S)}")

# ASCII, A
"""
This makes '\\w, \\W, \\b and \\B', '\\s' and '\\S' match only ASCII characters instead of the complete unicode which is
mainly used for unicode patterns and ignored by byte ones
"""

a = c.search('This has been so much fun learning!')
print(f"If this works it should look like this ----> {a, re.A} <---- YES it worked!")

# VERBOSE, X
"""
This might just be the most important flag as it lets you write clean and readable RE in a more flexible manner, when
specified any whitespace within the RE is ignored unless within a character class or has an unescaped backslash. It
lets you comment within the RE which is are marked by '#' just like a regular comment in python as long as it's neither
a character class or has an unescaped backslash in front of it. On a personal level though i would prefer to write the
RE in a single line and have regular comments above it explaining what it does.
"""

e = re.compile(r"""
\s*               # skip leading whitespace
(?P<header>[^:]+) # the header name
\s* :             # whitespace with a colon
(?P<value>.*?)    # the headers value along with using '*?' to lose the following trailing whitespace
\s*$              # trailing end of line whitespace
""", re.X)

# if you have comments above this explaining what it's for, looks much cleaner, to me anyway
e2 = re.compile(r'\w+[a-z][^\w{3}][0-9a-zA-Z]')
e3 = e2.search('If this works than i did something right!')

print(f"Even though the output is a little messy since it's in a single line in the code itself is much easier to\n"
      f"read and understand due to the breakdown of structure along with the comments\n----> {e}\nThis will print "
      f"cleanly on new lines, etc. if used within actual code though!\nif this works great! ----> {e3, re.X} <---- IT "
      f"WORKED!")

#######################################################################################################################
#                                                          FUNCTIONS                                                  #
#######################################################################################################################
print(f"\n{'Functions of RE':#^65}")

"""
The 4 main functions used with RE are '.split()', '.sub', '.findall()' and '.finditer()' which will be explained
more below.
"""
signs = r"test"
s = re.split('\s', 'I think it worked')

print(f"\n{'re.split()':#^45}")
"""
This just simply splits the string when being returned as a list
"""

print(f"The sentence should it at all the whitespaces: {s}")

print(f"\n{'re.sub()':#^45}")
"""
returns a string with all matching occurrences of the pattern are replaced by the replace string these functions
generally create and call the needed method as well as work as a storage for cache regarding objects that have been
complied, letting future calls won't repeatedly get passed through the same RE. When to use these would be within loops
as it saves time with function calls, but outside of loops doesn't make much difference.
"""

print(f"This should change 'test' to 'exam': '{signs}' should now be "
      f"{re.sub(signs, 'exam', 'the this was a really hard test')}")

print(f"\n{'re.findall()':#^45}")
"""
This is a simple and easy yet powerful way to obtain a list of all the substrings within the match pattern
"""

print(f"The list of 'test' words in the sentence: {re.findall(signs, 'Thetestofatestisreallyatest')}")

print(f"\n{'re.finditer()':#^45}")
"""
Findall is almost identical to Finditer except instead of a list finditer returns an iterator.
"""

print(f"The iterators of 'test' words in the sentence: {re.finditer(signs, 'Thetestofatestisreallyatest')}")

#######################################################################################################################
#                                                   Matching Objects                                                  #
#######################################################################################################################
"""
Most of the time when using RE the in this situation the letters and characters will match exactly with themselves,
however some characters are called 'special metacharacters' which don't match themselves. What they do instead is 
signal something different should be matched, or affect other portions of RE by repeating them or changing the meaning.

These [] are used for specifying character classes which is simply a set of characters you want to match together
such as [abc] which matches any characters 'a', 'b' or 'c'. You can list individual or a range of characters by giving
2 values splitting them using - , which looks like [a-c] which does the exact same thing as [abc], to match purely
lower case just use [a-z].
"""

################################################# re.Match ############################################################
print(f"\n{'Matching REs: re.match()':#^65}")
"""
Most of the time when using RE the in this situation the letters and characters will match exactly with themselves,
however some characters are called 'special metacharacters' which don't match themselves. What they do instead is 
signal something different should be matched, or affect other portions of RE by repeating them or changing the meaning.

These [] are used for specifying character classes which is simply a set of characters you want to match together
such as [abc] which matches any characters 'a', 'b' or 'c'. You can list individual or a range of characters by giving
2 values splitting them using - , which looks like [a-c] which does the exact same thing as [abc], to match purely
lower case just use [a-z].
"""

print(f"This should find the word 'test' ----> {re.match(signs, 'testtest')}")

################################################# re.Search ###########################################################
print(f"\n{'re.search()':#^65}")
"""
Returning an object with multiple other sub-functions mentioned above to get even more specific results from the data.
Group: returns what the REs matching results.
Start: returns the starting point of the match
End: returns the ending point of the match
Span: returns both the Start and End of the match
"""

signs = r"est"
match = re.search(signs, "thistestisfun")

if match: print(
    f"We will now get the sub-function results of 'thistestisfun':\nGroup: {match.group()}\nStart: {match.start()}\n"
    f"End: {match.end()}\nSpan: {match.span()}")

################################################# Search and Replace ##################################################
print(f"\n{'Search and Replace':#^65}")

"""
Normally you don't want to purely match a pattern but replace it with a variety of things being either a string or
function, to complete this the .sub() and .subn() methods are required. If the replacement is a string, backslash
escapes within it are processed, meaning \\n would be converted to its python form of a newline character, however \\&
and similar are left alone, back references such as \\6 become the substring matched by the matching group in the RE.

You can also use it as a function giving even more control, being called for every non-overlapping event of the pattern
when each call is made the function is passed an object argument to be matched, using the data to tell the desired
replacement string and return it. If requiring specific RE flags they must be used in either as a pattern object as the
the 1st () or embedded modifiers within the string 'sub("(?i)b+", "x", "bbbbBBBB"' should return 'x x'.

This is because:
'sub': returns the string obtained by replacing the leftmost non-overlapping event of the RE
'(?i)': the () is what captures whats inside it, where ? has no meaning but means i will determine the following
syntax's meaning of the remaining construct, which is 'ignore case'
'b+': simply means the 'b' character can be repeated 0 += times, however due to the ignore case all 'b' characters will
be ignored.
'x': is the only other character not being ignored so that with '+' will repeat twice
"""

################################################## Repeating ##########################################################
"""
When using RE you can not only match characters but make specific characters be repeated a specified number of times.
The 1st metacharacter to do this would be '*' as it won't match the character itself but instead tells the program to
repeat the previous character can be matched 0 += times instead of only once 'ca*t' will match 'ct' with '0 a' 
characters, 'cat' with '1 a' character and 'caaat' with '3 a' characters.

When using * it gets greedy trying to match the character as much as possible, if characters later on doesn't match it 
will back up and try again with less repeats. Using a[bcd]*b will match 'a' 0 += times from [bcd], ending finally with 
a 'b'.
"""

"Breakdown of string [abcbd] being matched against RE a[bcd]*b:"
#######################################################################################################################
#     Steps       #     Matched     #                                   Explanation                                   #
#######################################################################################################################
#      1          #       a         #     The 'a' in RE matches
#######################################################################################################################
#      2          #     abcbd       #     The engine matches '[bcd]*', going to the end of the string (far as possible)
#######################################################################################################################
#      3          #    Failure      #     Tries matching 'b', but current position is at the end of string, so fails
#######################################################################################################################
#      4          #     abcb        #     Back up, so that '[bcd]*' can match 1 less character
#######################################################################################################################
#      5          #    Failure      #     Tries 'b' again, but current position is at last character 'd' so fails
#######################################################################################################################
#      6          #     abc         #     Back up again, matching only 'bc' from '[bcd]*'
#######################################################################################################################
#      6          #     abcb        #     Tries 'b' again, current position is 'b' so it succeeds
#######################################################################################################################

"""
The above table explains the process of how RE uses repeats to find a match, if 'b' wasn't found it would keep
repeating the back up until it either matches it, tried 0 matching for [bcd]* and if that fails will determine that
the string doesn't match the RE at all.

Another metacharacter that repeats is '+' which is HIGHLY important to know the differences between this and * as
doesn't need the character to be present at all to be repeated, while + needs at least 1 occurrence, 'ca+t' matches
'cat' with '1 a' character, 'caaat' with '3 a' characters but won't even try to match 'ct' since it doesn't contain 'a'.
"""

"""
Other than + or * you could use '?' to also repeat characters, however it is more used as an optional match rather than
a specific match, as it matches 0 += 1 times 'home-?brew' will match either 'homebrew' or 'home-brew' only instead of
specific characters.

The most complicated repeat character would be '{m,n}' as 'm' and 'n' are decimal integers meaning there must be at 
least 'm' repeats and at most 'n' a/{1,3}b will match 'a/b', 'a//b' and 'a///b' disregarding 'ab' and 'a////b' as 'ab'
doesn't have any slashes and the matching will stop at the specified 3 slashes. {0,} is the same as *, {1,} is the same
as + and {0,1} is the same as ? however it's best to use *, + and ? as it looks cleaner and is much easier to read.
"""

#######################################################################################################################
#                                                     METACHARACTERS                                                  #
#######################################################################################################################
"""
Other than '\' metacharacters aren't active while used in classes, making [akm$] match any characters
'a', 'k', 'm' or '$'. The '$' is normally a meta but loses the title once put into a class. If you want to match
characters not included in the class, put ^ as the very first character [^5] making it exclude '5' but still matches
EVERY other character, but if you put it after another character [5^] it simply matches '5' or '^'.

When it comes to metacharacters the most important would be the backslash, which as mentioned above can keep it's title 
even when used within a class. This is due to python string literals the backslash can be followed by a variety of 
characters to signal different special actions, you could also use it to escape the metacharacters letting you still
match them within patterns, an example would be if you wanted to match '[' or '\' you would have to remove their 
special title by putting a backlash in front of them, letting you match them like any other character.
"""

print(f"List of Metacharacters:\nA set of characters: [], [a-m]\nSignaling a special sequence: \\, \\d\nAny character: "
      f"., he..o\nStarts with: ^, ^hello\nEnds with: $, hello$\n0 or more occurrences: *, he.*o\n"
      f"1 or more occurrences: +, he.+o\n0 or 1 occurrences: ?, he.?o\nThe exact specified numbered occurrences: "
      f"{'{}'}, he.{2}o\nEither or: |, falls|stays\nCapture and Group: ()")

print(f"\n{'Using .':#^45}")
patterns = r"gr.y"  # makes anything between 'gr' and 'y' match
if re.match(patterns, "grey"): print(f"Characters match")
if re.match(patterns, "gray"): print(f"Characters match")
if not re.match(patterns, "black"): print(f"Characters don't match")

print(f"\n{'Using ^ and $':#^45}")
p = r"^gr.y$"  # string should start with 'gr' and end with 'y
if re.match(patterns, "grey"): print(f"Characters match")
if re.match(patterns, "gray"): print(f"Characters match")
if not re.match(patterns, "stingray"): print(f"Characters don't match")

print(f"\n{'Using *':#^45}")
a = r"egg(spam)*"  # string starts with 'egg' matching 0 or more 'spams' after it
if re.match(a, "egg"): print(f"Characters match")
if re.match(a, "eggspamspamegg"): print(f"Characters match")
if not re.match(a, "spam"): print(f"Characters don't match")

print(f"\n{'Using +':#^45}")
t = r"g+"  # string starts with 'g' matching 1 or more 'g's after it
if re.match(t, "g"): print(f"Characters match")
if re.match(t, "gggg"): print(f"Characters match")
if not re.match(t, "hang"): print(f"Characters don't match")

print(f"\n{'Using ?':#^45}")
t = r"ice(-)?cream"  # the () captures - while the ? repeats - 0 or 1 time
if re.match(t, "ice-cream"): print(f"Characters match")
if re.match(t, "icecream"): print(f"Characters match")
if not re.match(t, "ice--cream"): print(f"Characters don't match")

print(f"\n{'Using {}':#^45}")
e = r"9{1,3}$"  # matches the string before {} the amount of times specified in {}
if re.match(e, "9"): print(f"Characters match")
if re.match(e, "999"): print(f"Characters match")
if not re.match(e, "9999"): print(f"Characters don't match")

print(f"\n{'Matching Passwords':#^45}")
password = input('Please Enter a Password: ')
pattern = r"\w*[a-zA-Z]\w*[0-9]\w*"

if re.match(pattern, password): print(f"Your password is now created!")

#######################################################################################################################
#                                                         CHARACTERS                                                  #
#######################################################################################################################
print(f"\n{'RE Characters':#^65}")

"""
Lets you match specific sets of characters that are specified within []
"""

print(f"List of Characters:\nReturns a specific match of characters 'a', 'r' or 'n': [arn], "
      f"{re.findall('[arn]', 'Its hot right now')}\nReturns any lower case between 'a' and 'n': "
      f"[a-n], {re.findall('[a-n]', 'Its hot right now')}\nReturns everything but 'a', 'r' and 'n': [^arn], "
      f"{re.findall('[^arn]', 'Its hot right now')}\nReturns a specified match of digits '0', '1', '2' or '3': "
      f"[01234], {re.findall('[01234]', '9482071864')}\nDoes the same as [a-n] but between '0' and '9': [0-9], "
      f"{re.findall('[0-9]', '9482071864')}\nReturns any 2-digit numbers from '00' to '59': [0-5][0-9], "
      f"{re.findall('[0-5][0-9]', '009482071864')}\nReturns a match for both upper or lower case from 'a' to 'z': "
      f"[a-zA-Z], {re.findall('[a-zA-Z]', 'Its hot right now')}\nReturns a match for any '+' in the string: [+], "
      f"{re.findall('[+]', 'Its + hot + right + now')}")

print(f"\n{'Using []':#^45}")
pattern = r"[aeiou]"  # matches any of the characters within []
if re.search(pattern, 'grey'): print(f"Characters match")
if re.search(pattern, 'apple'): print(f"Characters match")
if not re.search(pattern, "myths"): print(f"Characters don't match")

print(f"\n{'Using [][][]':#^45}")
patter = r"[A-Z][A-Z][0-9]"  # matches 2 upper case letters followed by a number from 0-9
if re.search(patter, 'SR9'): print(f"Characters match")
if re.search(patter, 'S9'): print(f"Characters match")
if not re.search(patter, "sr9"): print(f"Characters don't match")

print(f"\n{'Using [^]':#^45}")
patters = r"[^A-Z]"  # matches anything except upper letters from a-z
if re.search(patters, 'this is really fun'): print(f"Characters match")
if re.search(patters, 'ThIsReAlLyFuN123'): print(f"Characters match")
if not re.search(patters, "THISISREALLYFUN"): print(f"Characters don't match")

#######################################################################################################################
#                                                         GROUPS                                                      #
#######################################################################################################################
print(f"\n{'Groups':#^65}")

"""
More than likely you'll need to get more data then just a match when using RE so to get around that simply write REs
which matches an entire header line, including one group matching the header self with another group matching the value.
We have touched on .group() before but will now go in to it deeper as well as .groups(), unlike the .group() method 
this will return the output as a tuple.

Grouping can have sub-groups which are numbered from left to right and 1 upwards, and can also be nested, simply
determine the number by counting the opening () from left to right. Back references are very handy as they specify that
the contents of a previously captured group has to be found at the current location within the string meaning '\1' will
work if the exact content of group 1 is found in the current position.
"""

pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, 'abcdefghijklmnopqrstuvwyxz')

if match:
    print(f"returning all the matches: {match.group()}")
    print(f"does the same as without having a number: {match.group(0)}")
    print(f"returns the 1st (): {match.group(1)}")
    print(f"returns the 2nd (): {match.group(2)}")
    print(f"returns all ()s: {match.groups()}")

################################################ Non-capturing and Named Groups #######################################
print(f"\n{'Non-Capturing and Named Groups':#^65}")
"""
More advanced REs might contain multiple groups some capturing the sub-string of interest while others group and
structure the RE, when this happens it could be hard to keep track of the numbers. Luckily there are a couple of 
similar to RE extensions in regards to common syntax. In the PERL language they use ? in front of the first ( of () to
get rid of compatibility issues, making (?=same) and (?:same) too different expressions with ?= being a positive
lookahead assertion and ?: being a non-capturing group containing the subexpression 'same'. Python adopts several of 
PERLs extensions adding their own extension syntax to PERLs marked with a 'P' after ? to indicate it's specifically a
python extension.

?: becomes greatly helpful when wanting to modify existing groups without changing the numbering of them, it doesn't
make it any slower either, on top of those things using it can have the same qualities as regular grouping including
the use of metacharacters. Most importantly is the fact you can use naming to refer to an index rather than purely
numbering, to use it simply put P after ?. If that isn't enough you can also get data as a dictionary via '.groupdict()'
"""

"""
When it comes to named groups you can easily reference a specific group by adding W with a number 'W1', to ensure the
self should be matched at the current point using ?P= is the way to do it, this makes reading it much easier and look
even cleaner.
"""

pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, 'abcdefghijklmnopqrstuvwyxz')

if match: print(f"This will print whats after <>: {match.group('first')}"), print(f"{match.groups()}")

################################################# Lookahead Assertions ################################################
print(f"\n{'Lookahead Assertions':#^65}")
"""
These can be both positive and negative forms which are included as a zer0-width assertion. This is a positive '?='
that succeeds if the contained RE successfully matches the current position, stopping once matched making the remainder
of the pattern be tried where the assertion started. While this is a negative '?!' which succeeds if the RE doesn't
match the current position.

To break down a filename separating the self from the extension using '.' where 'python.py' would be 'python' as the
base self and '.py' being the extension you'll have to write the RE '.*[.].*$' below is a breakdown of why this is:
'.' needs to be in [] as it's a metacharacter so this will make it match only that specific character.
'*' will make the previous character repeat itself 0 += times
'$' ensures the remaining string is included in the extension
Having this will let you separate any files that have '.' within it.
"""

"""
Using positive lookaheads can end up getting VERY confusing and messy, possibly ending up looking like this
'.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$' this complicated RE simply makes '^a' and '^t' optional to allow for extensions
less than 3 characters to be allowed, otherwise it'll raise an error.

To get around this and continue making nice clean code along with easier to understand REs using negative lookaheads is
your best option as it looks like '.*[.](?!py$)[^.]*$' broken down means if the file isn't .py then continue with the
rest of the pattern which looks so much cleaner than the previous one used. The final $ is to ensure other extensions
with py in the self still parse through, while [^.]* ensures it runs with files including multiple '.' in the self.
"""

#######################################################################################################################
#                                                    SPECIAL SEQUENCES                                                #
#######################################################################################################################
print(f"\n{'Special Sequences':#^65}")
"""
When starting the sequence with a backslash some are predefined sets of characters like digits, letters and anything
that isn't a whitespace '\\w' (ignore the 1st '\')  will match any character within the alphabet, which is the same as
[a-zA-Z0-9_] if RE was expressed in a bytes pattern, while if used as a string pattern will match all the characters
considered to be letters within 'Unicode database' provided by the 'unicodedata' module, to use a more restricted form
of it within a string pattern you'll have to supply the 're.ASCII' flag to it when compiling RE.

The below sequences can be used within character classes. To match ANY character including new lines using 're.DOTALL'
will do that, otherwise using a regular '.' will match ANY character EXCEPT new lines.
"""

print(f"\\d is the same as: [0-9]\n\\D is the same as: [^0-9]\n\\s is the same as: [ \\t\\n\\r\\f\\v]\n\\S is the same "
      f"as: [^ \\t\\n\\r\\f\\v]\n\\w is the same as: [a-zA-Z0-9_]\n\\W is the same as: [^a-zA-Z0-9_]")

print(f"\n{'Example 1':#^65}")
pattern = r"(.+) \1"  # will use (.+) to match the same string 1+ times, while \1 is the group number
match = re.match(pattern, 'word word')
ma = re.match(pattern, '?! ?!')
m = re.match(pattern, 'abc cde')  # won't match because the 2 words don't match

if match: print(f"Characters match")
if ma: print(f"Characters match")
if not m: print(f"Characters don't match")

print(f"\n{'Example 2':#^65}")
pattern = r"(\D+\d)"  # matches 1+ non-numeric characters followed by a digit
match = re.match(pattern, 'Hi 123!')
ma = re.match(pattern, '1, 23, 456!')
m = re.match(pattern, ' ! $?')

if match: print(f"Characters match")
if ma: print(f"Characters match")
if not m: print(f"Characters don't match")

#######################################################################################################################
#                                                    EMAIL EXTRACTION                                                 #
#######################################################################################################################
print(f"\n{'Email Extraction':#^65}")

"""
This is using all the above information to gather email data from a string
"""

p = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"  # [\w\.-] matches 1+ word, dot or dash characters
str = "Please email me on python.study@outlook.com for more details"
match = re.search(p, str)

if match: print(f"We just gathered the data, the email: {match.group()}")

#######################################################################################################################
#                                                    EXERCISE                                                         #
#######################################################################################################################
print(f"\n{'Exercise Practice: Number Validator':#^65}")

"""
[789]: matches any characters relating to '7', '8' or '9'
\d: matches from 0-9
{7}: matches the characters [789] and \d 7 times
$: ends the matching process making it end at 8 number checks
"""
valid_check = re.search(r'[789]\d{7}$')  # makes it so the number only starts with 1. 8 or 9 with exactly 8 digits
input('Please enter your phone number: ')

if valid_check: print(f"Phone number is valid!")
