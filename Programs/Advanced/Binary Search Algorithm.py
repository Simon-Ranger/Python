# Created by Simon Ranger : December 8th 2022

"""
A more advanced project designed around binary search algorithm.

How to Use:
1. Follow input directions when prompt.

Desired Output:
Created a list of numbers determined by the user input with every succeeding number being a difference of 2 between
them. Checks if user input is included and removed the half that wasn't.
"""

# Imports required

# Setting the global variable
nums = []


# Determining the Numbers
def determiningNumbers():
    # Asking user for number of entries
    ask = int(input(f"How many numbers do you want to enter? "))
    int(input(f"Enter {ask} numbers: "))

    # Looping the user input to insert the numbers
    [nums.insert(i, int(input())) for i in range(ask)]

    # Looping through the numbers with adding/subtracting the value
    for i in range(ask - 1):
        for x in range(ask - i - 1):
            if nums[x] > nums[x + 1]:
                amount = nums[x]
                nums[x] = nums[x + 1]
                nums[x + 1] = amount

    # Print and Loop the list of numbers
    print(f"\nThe list is: ")
    [print(f"{nums[i]}") for i in range(ask)]


# Searching for the Number
def numberSearch(nums):
    # Asking user for number to search
    int(input(f"Enter a number to search: "))

    # Setting the variables
    first = 0
    last = nums - 1
    middle = int(first + last) / 2  # making the numbers differ by 2
    user = int(input())
    check = 0

    # Looping through the variables
    for first in range(last + 1):
        if nums[middle] < user: first = middle + 1
        elif nums == user:
            print(f"{user} Found at position: {middle + 1}")
            check = 1
            break
        else:
            last = middle - 1

        return f"{last}"

    if check != 1: print(f"{user} is Not Found in list")

    # Removes the half that wasn't found and returns the found amount
