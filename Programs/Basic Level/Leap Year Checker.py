"""
A very simple calculator to determine if it was a leap year or not

How to Play:
1. Enter a year when prompt

Desired Output:
To determine if the year given is a leap year or not.
"""

if __name__ == "__main__":
    date = int(input("Please enter a year: "))

    print(f"{date} is a leap year!") if date % 4 == 0 else print(f"{date} is not a leap year!")

