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
from pandas import DataFrame as df, read_csv, DataFrame
import numpy as np
from matplotlib import pyplot as plt
from datetime import date

# create empty lists
GoodsOrServices: list | str = []
Prices: list | float = []
Dates: list | date = []
ExpenseType: list | str = []


# funct adding data to lists
def addingData(goodsOrServices: str, prices: int | float, dates, expenseType: str) -> None:
    # appending to the lists
    GoodsOrServices.append(goodsOrServices)
    Prices.append(prices)
    Dates.append(dates)
    ExpenseType.append(expenseType)


def reportData() -> DataFrame:
    expenseType = ""

    # creating the dataframe
    report = df()
    report["GoodsOfServices"] = GoodsOrServices
    report["Prices"] = Prices
    report["Dates"] = Dates
    report["ExpenseType"] = ExpenseType
    report.to_csv("Expenses.csv")

    # creating an array to loop through the data and pull the data for each section
    FoodP = []
    HouseP = []
    TravelP = []

    # reads the file that was created above
    with open("Expenses.csv"):
        read_csv("Expenses.csv", skiprows=1)

    for _ in enumerate(report):
        if expenseType == "Food":
            Prices.append(FoodP)
        elif expenseType == "Household":
            Prices.append(HouseP)
        elif expenseType == "Travel":
            Prices.append(TravelP)
        elif _:
            print(f"Error: Something went wrong!")

    # putting the data into a graph
    plt.plot(report)
    plt.legend()
    plt.show()

    return report


def main():
    # option menu for the user
    truth: int = 1
    user: str = (input(f"Please enter your name: "))

    while truth != 0:
        options = int(
            input(f"Welcome {user} to this interactive expense tracker!\nPlease select an option below:\n1. Add "
                  f"Food Expenses\n2. Household expenses\n3. Travel Expenses\n4. Display and Save the "
                  f"Expense Report\n0. Exit\nPlease enter the choice here: "))

        match options:
            case 0:
                exit(f"Thank you for using the Expense Tracker. See you next time!")
            case 1:
                print(f"Adding Food\n")
                expenseType = "Food"
            case 2:
                print(f"Adding Household\n")
                expenseType = "Household"
            case 3:
                print(f"Adding Travel\n")
                expenseType = "Travel"
            case 4:
                reportData()

        # lets the user enter the data
        if options == 1 or options == 2 or options == 3:
            goodsOrservices = str(input(f"Enter the goods or services for the expense type {expenseType}:\n")).strip()
            price = float(input(f"Enter the price of the goods or service:\n"))
            today = date.today()
            addingData(goodsOrservices, price, today, expenseType)


if __name__ == "__main__":
    main()
