# Created by Simon Ranger : November 17th 2022

"""
A very simple calculator to determine if it was a leap year or not

How to Play:
1. Enter a year when prompt

Desired Output:
To determine if the year given is a leap year or not.
"""

if __name__ == "__main__":
    date = int(input("Please enter a year: "))

    if date % 400 == 0 or date % 100 != 0 and date % 4 == 0:
        print(f"{date} is a leap year")
    else:
        print(f"{date}, is not a leap year")


