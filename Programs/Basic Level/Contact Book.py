# Created by Simon Ranger : November 15th 2022

"""
This project is a simple Contact Book that can store, edit, search and remove contacts.

How to Play:
1. Enter the amount of people you want to add. If you don't want to add anyone type 0 to go straight to the option menu
2. Select an option by following the prompt
3. Enter the data when prompt

Desired Output:
Users can create their own contact book that will be saved letting them use it regularly.
"""


import sys

person = {}


def AddContacts(contacts):
    while True:
        contactAmount = input("Please enter the number of people you want to add: ")

        try:
            contactAmount = int(contactAmount)
        except ValueError:
            print(f"{contactAmount} is not a number!")
            continue
        else: break

    if contactAmount < 1: return

    print(f"All mandatory fields will include *")

    for i in range(contactAmount):
        person['name'] = input("Enter a name*: ")
        person['number'] = int(input("Enter a number*: "))
        person['email'] = input("Enter an email: ")
        person['age'] = input("Enter a D.O.B (mm/dd/yy): ")
        person['category'] = input("Enter what category the contact is (Family/Friends/Work/Other)*: ")

        contacts.append(person)
    print(f"Your contacts are:\n{contacts}")


def SearchContacts(contacts):
    name = input("Enter the name you want to remove: ")

    for i, contact in enumerate(contacts):
        if contact[0] == name:
            print(f"You successfully found {contact[i]}")
            return contacts[i]
    else:
        print(f"You don't have a {name} in your contacts")

    print(f"Returning to the main menu...")


def UpdateContacts(contacts):
    ShowContacts(contacts)
    checking = input("Enter the contact you want to edit: ")

    for i, contact in enumerate(contacts):
        if contact == checking:
            print(f"Ready to edit {checking}...If data is staying the same, just re-type the existing data!")
            return contacts[i]

    person["name"] = input("Please enter the new name: ")
    person["number"] = int(input("Please enter the new number: "))
    person["email"] = input("Please enter the new email: ")
    person["age"] = input("Please enter the new D.O.B: ")
    person["category"] = input("Enter what category the contact is (Family/Friends/Work/Other): ")

    print(f"You have successfully updated data of {checking} ===> {person}")


def ShowContacts(contacts):
    print(f"Your contacts are:\n{contacts}")


def ClearContacts(contacts):
    answer = input("Are you sure you want to clear your contact book? (Y/N): ")

    if answer.lower() == "y":
        contacts.clear()
        print(f"You have removed all contacts...")
    elif answer.lower() == "n":
        return

    print(f"Returning to the main menu...")


def RemoveContact(contacts):
    name = input("Enter the name you want to remove: ")

    for i, contact in enumerate(contacts):
        if contact[0] == name:
            del contacts[i]
            print(f"You have successfully removed {name}")
    else:
        print(f"You don't have a {name} in your contacts")

    print(f"Returning to the main menu...")


def Options(contacts, option):
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

    if option == 1: AddContacts(contacts)
    elif option == 2: SearchContacts(contacts)
    elif option == 3: UpdateContacts(contacts)
    elif option == 4: RemoveContact(contacts)
    elif option == 5: ShowContacts(contacts)
    elif option == 6: ClearContacts(contacts)
    elif option == 7: sys.exit(f"Thank you for using this contact Book! Have a great day!")


def Menu():
    print(f"\t\t\t{'Contact Book':*^100}\nYour options are:\n1. Add a Contact\n2. Searching Contacts\n"
          f"3. Edit Contacts\n4. Delete Contacts\n5. View Contacts\n6. Delete All Contacts\n7. Close the Book")


def Main():
    contacts = []

    print(f"Welcome to your new Contact Book! Hope you find it easy to navigate!")
    AddContacts(contacts)

    while True:
        Menu()
        option = input("Please select an option: ")
        Options(contacts, option)


if __name__ == "__main__":
    Main()
