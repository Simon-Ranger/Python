# Created by Simon Ranger : December 8th 2022

"""
Uses the binary tree module to automate everything into a visual display.

How to Use:
1. Follow input directions when prompt.
2. Select a number between 0 - 9

Desired Output:
Prints out a binary tree for the specified number from the user
"""

# Imports required
from binarytree import bst


def binaryTree() -> None:
    # Asking user for number of entries
    user = int(input(f"Enter the height you want:\n"))
    search = bst(height=user)
    print(f"Binary Search Tree of your choice is:\n{search}")


"""
Creates its own binary search without the module

How to Use:
1. Follow the prompt

Desired Output:
Created a list of numbers determined by the user input with every succeeding number being a difference of 2 between
them. Checks if user input is included and removed the half that wasn't.
"""


def binarySearchAlgorithm(user: list[int], amount: int, isSorted: bool = False) -> int:
    middle = len(user) // 2

    if not isSorted: user = sorted(user)
    result = user[middle]

    if len(user) == 1:
        if user[0] == result: return 0
        else: return -1

    if result == amount: return amount
    elif result < amount: return binarySearchAlgorithm(user[:middle - 1], amount, True)
    else: return binarySearchAlgorithm(user[:middle + 1], amount, True)


if __name__ == '__main__':
    binaryTree()
    print(binarySearchAlgorithm(user=[30], amount=3, isSorted=True))

