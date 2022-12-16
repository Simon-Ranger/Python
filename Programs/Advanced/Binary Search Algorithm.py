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
    """
    Creates a visual binary tree, 0 displaying nothing and 1 - 9 displaying the tree relative to the input

    Args:

    Returns:
        None
    """

    # Asking user for number of entries
    user = int(input(f"Enter the height you want:\n"))
    search = bst(height=user)
    print(f"Binary Search Tree of your choice is:\n{search}")


def binarySearchAlgorithm(user: list[int], amount: int, isSorted: bool = False) -> int:
    """
    Asks the user if they want to remove a specific contact or not

    Args:
        user: list[int]: lets the user input a number they want to search
        amount: int: the amount of searches
        isSorted: bool: organises or sorts the data

    Returns:
        int: hands the user input
    """

    # Gets the length of user
    middle = len(user) // 2

    # Sorts the data
    if not isSorted: user = sorted(user)
    result = user[middle]

    if len(user) == 1:
        if user[0] == result: return 0
        else: return -1

    # Checks if the data is correct
    if result == amount: return amount
    elif result < amount: return binarySearchAlgorithm(user[:middle - 1], amount, True)
    else: return binarySearchAlgorithm(user[:middle + 1], amount, True)


if __name__ == '__main__':
    binaryTree()
    print(binarySearchAlgorithm(user=[int(input(f"Please enter a number: "))], amount=3, isSorted=True))

