# Created by Simon Ranger : November 15th 2022

"""
This project is a simple Contact Book that can store, edit, search and remove contacts.

How to Use:
1. Enter the amount of people you want to add. If you don't want to add anyone type 0 to go straight to the option menu
2. Select an option by following the prompt
3. Enter the data when prompt

Desired Output:
Users can create their own contact book that will be saved letting them use it regularly.
"""

# Imports required
import sys
from typing import List

# Creating an empty dictionary
person = {}


def AddContacts(contacts: list[dict]) -> list:
    """
    Asks the user how many people they want to add to the contact book

    Args:
        contacts: list[dict] : stores the contacts information

    Returns:
        list: lets the user add contacts to the list
    """

    # Loops through user input
    while True:
        contactAmount = str(input("Please enter the number of people you want to add: "))

        # Tries to run the command and catch any errors that happen
        try:
            contactAmount = int(contactAmount)
        except ValueError:
            print(f"{contactAmount} is not a number!")
            continue
        else: break

    if contactAmount < 1: return contacts

    print(f"All mandatory fields will include *")

    # Loops through each contact to gather the data from the user
    for i in range(contactAmount):
        person['name'] = str(input("Enter a name*: "))
        person['number'] = int(input("Enter a number*: "))
        person['email'] = str(input("Enter an email: "))
        person['age'] = str(input("Enter a D.O.B (mm/dd/yy): "))
        person['category'] = str(input("Enter what category the contact is (Family/Friends/Work/Other)*: "))

        # Updates the dictionary with the gathered data
        contacts.append(person)
    print(f"Your contacts are:\n{contacts}")


def SearchContacts(contacts: list[dict]) -> dict:
    """
    Searches through the contact list to determine if the contact user requested in there or not, relaying the answer
    back to the user.

    Args:
        contacts: list[dict]: used to search for the name

    Returns:
        dict: dict: holds all the user data to be searched
    """

    name = str(input("Enter the name you want to find: "))

    # Loops through the dictionary to find the name
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            print(f"You successfully found {contact[i]}")
            return contacts[i]
    else:
        print(f"You don't have a {name} in your contacts")

    # Prints a message and then returns to the main menu
    print(f"Returning to the main menu...")
    Menu()


def UpdateContacts(contacts: list[dict]) -> dict:
    """
    Updates the contact list with new data from the user

    Args:
        contacts: list[dict]: used to display the list of names

    Returns:
        dict: holds all the user data and lets it be updated
    """

    # Displays the contact list
    ShowContacts(contacts)
    checking = str(input("Enter the contact you want to edit: "))

    # Loops through the list to check if contact is able to be edited
    for i, contact in enumerate(contacts):
        if contact == checking:
            print(f"Ready to edit {checking}...If data is staying the same, just re-type the existing data!")
            return contacts[i]

    person["name"] = str(input("Please enter the new name: "))
    person["number"] = int(input("Please enter the new number: "))
    person["email"] = str(input("Please enter the new email: "))
    person["age"] = str(input("Please enter the new D.O.B: "))
    person["category"] = str(input("Enter what category the contact is (Family/Friends/Work/Other): "))

    print(f"You have successfully updated data of {checking} ===> {person}")


def ShowContacts(contacts: list[dict]) -> None:
    """
    Displays the contact list

    Args:
        contacts: list[dict]: used to display the list of names

    Returns:
        None
    """

    print(f"Your contacts are:\n{contacts}")


def ClearContacts(contacts: list[dict]) -> list:
    """
    Asks the user if they want to completely clear their contact book

    Args:
        contacts: list[dict]: used to clear the whole dictionary

    Returns:
        list: holds all the user data and lets it be cleared
    """

    answer = str(input("Are you sure you want to clear your contact book? (y/n): "))

    # Checks to see if the user wants to clear the contact book or not
    if answer.lower() == "y":
        contacts.clear()
        print(f"You have removed all contacts...")
    elif answer.lower() == "n":
        return contacts

    print(f"Returning to the main menu...")


def RemoveContact(contacts: list[dict]) -> None:
    """
    Asks the user if they want to remove a specific contact or not

    Args:
        contacts: list[dict]: used to remove a contact

    Returns:
        None
    """

    name = input("Enter the name you want to remove: ")

    # Loops through the contact list and if it finds the name removes the contact
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            del contacts[i]
            print(f"You have successfully removed {name}")
    else:
        print(f"You don't have a {name} in your contacts")

    print(f"Returning to the main menu...")


def Options(contacts: list[dict], option: int) -> None:
    """
    Asks the user if they want to remove a specific contact or not

    Args:
        contacts: list[dict]: used to hold the contacts
        option: int: links the user choice with the respective function

    Returns:
        None
    """

    # Loops through the users options
    while True:
        try: option = int(option)
        except ValueError:
            print(f"{option} has to be a number!")
            option = int(input("Please select an option: "))
        else:
            if option < 1 or option > 7:
                print(f"Select an option from 1 - 7!")
                option = int(input("Please select an option: "))
            else: break

    # Directs the user input to the allocated function
    if option == 1: AddContacts(contacts)
    elif option == 2: SearchContacts(contacts)
    elif option == 3: UpdateContacts(contacts)
    elif option == 4: RemoveContact(contacts)
    elif option == 5: ShowContacts(contacts)
    elif option == 6: ClearContacts(contacts)
    elif option == 7: sys.exit(f"Thank you for using this contact Book! Have a great day!")


if __name__ == "__main__":
    def Main() -> None:
        """
        Asks the user if they want to remove a specific contact or not

        Args:

        Returns:
            None
        """

        # Creates an empty list
        contacts = []

        # Welcomes the user then directs to AddContacts()
        print(f"Welcome to your new Contact Book! Hope you find it easy to navigate!")
        AddContacts(contacts)

        # Loops through to check if user input is true, lets user select an option then directs to Options()
        while True:
            Menu()
            option = int(input("Please select an option: "))
            Options(contacts, option)

    def Menu():
        """
        The main menu

        Args:

        Returns:
            None
        """

        # Displays the options the user can select from
        print(f"\t\t\t{'Contact Book':*^100}\nYour options are:\n1. Add a Contact\n2. Searching Contacts\n"
              f"3. Edit Contacts\n4. Delete Contacts\n5. View Contacts\n6. Delete All Contacts\n7. Close the Book")


