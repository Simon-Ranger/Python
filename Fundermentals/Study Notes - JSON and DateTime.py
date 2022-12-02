"""
This file contains in the following order:
1. JSON:
    Loading
    Formatting
2. DATETIME:
    Dates and Objects
    Strftime
"""

#######################################################################################################################
#                                                          JSON                                                       #
#######################################################################################################################
""""
Used for storing and exchanging data that's been written in text using JavaScript object notation. Very useful
when wanting to expose an API however using a malicious JSON script could consume alot of CPU and memory preventing the
parse to work fully.
"""

############################################### Loading ###############################################################
print(f"\n{'Loading a JSON File':#^65}")
import json

sample = '{"name1":"Hello,", "name2":"World"}'  # contains the data in JSON

data = json.loads(sample)   # loads the JSON data from "sample" assigning it to the variable data
print(f"{data['name1']} {data['name2']}")

################################################ Formatting ###########################################################
print(f"\n{'Formatting a JSON File':#^65}")
MyDict = {  # the example dictionary in python
    "Name": "Simon",
    "Age": 32,
    "Job": "Teacher",
    "Rich": False
}
unformatted = json.dumps(MyDict)    # prints the data without formatting it, prints in 1 line
formatted = json.dumps(   # using dumps to convert the python into JSON in a formatted format
    MyDict,
    indent=4,   # defines how many indents are used
    separators=(". ", " = "),   # changes the seperator, could be a period, comma or anything really
    sort_keys=True  # sorts the output dictionaries by key, making it look exactly like this format when printed
)
print(f"We have 2 dictionaries, one that is not yet formatted ----> {unformatted} <----\n"
      f"and one that is formatted ----> {formatted} <----\n")

# Reading a File #
f = open("JSON test script.py")
data = json.load(f)

print(f"Gets the data from a completely different file!\n----> {[i for i in data['employee_details']]}")
f.close()

#######################################################################################################################
#                                                 DATETIME                                                            #
#######################################################################################################################
"""
Python doesn't have a date data type generally, so you'll need to import a module called datetime for date related
code to function properly. This module has several ways to display the time, date, etc.
"""

##################################################### Dates and Objects ###############################################
print(f"\n{'Dating Objects':#^65}")
"""If you want to make a specific time you can remove the 'now' and put what you want within the ()"""

from datetime import datetime

RealTime, Date = datetime.now(), datetime.now()  # displays the complete date/time at the current time the code was run

NewDate = Date.replace(year=1990, month=12, day=1, hour=17, minute=30)  # replaces the date and time with the new data
Date = NewDate

print(f"The current time is {RealTime} but that isn't fun so now it's {Date}")

###################################################### Strftime #######################################################
print(f"\n{'The strftime Method':#^65}")
"""
To format date objects into strings that are readable, use this method as it takes a single parameter format to
determine the format you want returned.
"""

from datetime import datetime

now = datetime.now()
current = now.strftime("%m/%d/%Y %H:%M:%S %p")  # turns the values into a string before reading the data
print(f"The current time and date is: {current}")
