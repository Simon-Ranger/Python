# Created by Simon Ranger : December 15th 2022

"""
A general expense tracker that is displayed in table format as well as statistical format

How to use:
1. when prompt enter the data you want to be stored

Desired Output:
The user can add to a variety of lists relating to what expenses they wanted, food, general, etc. which will be both
displayed in a file and the terminal.
"""

# Imports required
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Creating empty lists
GOODS_OR_SERVICES: list = []
PRICES: list = []
DATES: list = []
EXPENSE_TYPES: list = []


def adding_data(goods_or_services: str, prices: float, dates: str, expense_types: str) -> None:
    """
    Simply just appends everything together to be used throughout the script

    Args:
        goods_or_services: str : the item or service the user inputs
        prices: float : the cost of the goods_or_services
        dates: str : when the data was put into the file
        expense_types: str : category choice (food, household, travel, etc.)

    Returns:
        None
    """

    # Appending variables to the empty lists
    GOODS_OR_SERVICES.append(goods_or_services)
    PRICES.append(prices)
    DATES.append(dates)
    EXPENSE_TYPES.append(expense_types)


def main() -> None:
    """
    This is the main part of the script that runs all the menu options and user inputs. The while loop with if
    statements runs through the user choices, allocating the type of expense depending on the selected choice, the
    last if statement lets the user input the data where prompt.

    Args:

    Returns:
        None
    """
    # Creating the main menu

    # Loops through the user options allocating the expense type
    name = str(input(f"Please enter your name: "))
    truth = 1

    while truth != 0:
        print(f"Welcome {name} to this interactive expense tracker!\nPlease select an option below:\n1. Add "
              f"Food Expenses\n2. Household expenses\n3. Travel Expenses\n4. Display and Save the "
              f"Expense Report\n0. Exit\n")

        truth = int(input(f"Please select an option: "))

        if truth == 0:
            exit(f"Thank you {name} for using the expense tracker, have a good day!")
        elif truth == 1:
            print(f"Adding food items to the list...")
            expense_types = "Food"
        elif truth == 2:
            print(f"Adding household items to the list...")
            expense_types = "Household"
        elif truth == 3:
            print(f"Adding travel costs to the list...")
            expense_types = "Travel"
        elif truth == 4:
            report_data()
        else:
            print(f"Error: Please type 0 - 4 only...")

        # Let the user input the data they want to save
        if truth == 1 or truth == 2 or truth == 3:
            goods_or_services = str(input(f"Enter the {expense_types} items or services:\n"))
            price = float(input(f"Enter the price of the {goods_or_services}:\n₩"))
            now = datetime.now()
            date_time = now.strftime("%m/%d/%Y %H:%M:%S %p")
            adding_data(goods_or_services, price, date_time, expense_types)


def report_data() -> pd.DataFrame:
    """
    Creates the dataframes, putting it into a file, create an array to hold all the prices then adding them. Read from
    the file and put all the finalised data into a bar graph

    Args:

    Returns:
        DataFrame as df : created the dataframe from pandas to store and display the user data in table format
    """

    # Creating the dataframe
    report = pd.DataFrame()
    report["GOODS_OR_SERVICES"] = GOODS_OR_SERVICES
    report["PRICES"] = PRICES
    report["DATES"] = DATES
    report["EXPENSE_TYPES"] = EXPENSE_TYPES

    # Save the data to a file
    report.to_csv("Expenses.csv")
    # Show the data
    print(f"Your current expenses are\n{report}")

    # Calculates the total sum of the cost
    Food_Price = np.sum(report["PRICES"][report["EXPENSE_TYPES"] == "Food"])
    House_Price = np.sum(report["PRICES"][report["EXPENSE_TYPES"] == "Household"])
    Travel_Price = np.sum(report["PRICES"][report["EXPENSE_TYPES"] == "Travel"])

    # Putting the data into a graph
    x_values = ["Food", "Household", "Travel"]
    y_values = [Food_Price, House_Price, Travel_Price]

    plt.bar(x_values, y_values)
    plt.title("Expenses")
    plt.xlabel("Category")
    plt.ylabel("Prices(₩)")
    plt.show()

    return report


if __name__ == "__main__":
    main()
