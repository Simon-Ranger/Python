# Created by Simon Ranger : November 23rd 2022

"""
This project is a basic to advanced app that lets you connect to the pizza hut website without actually typing anything
into the browser itself.

How to Use:
1. to access the site, click "welcome to pizza hut"
2. click on the tab/link to direct to the page you want
3. fill in the information where required

Desired Output:
Users can pretend to buy a meal from pizza hut by going through the same steps they would on the real site, then
if wanting can go to the real site and actually order it on there.
"""

# The imports required
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import requests

# The url the app will connect to
url = "https://www.pizzahut.co.kr/"
# Initiates the code
pizza = tk.Tk()
# Title of the app
pizza.title("Welcome to the Pizza Hut App")
# Size of the window
pizza.geometry("400x500")
# Colour of the background for the app
pizza.configure(background="red")


# Lets the app open the url
def open_url(event):
    webbrowser.open_new_tab(url)


# Button to direct you to the url
button = tk.Button(pizza, text="Click here for the real site!")
button.grid(column=0, row=0)
button.configure(fg="white", bg="black")

# Setting the size options
option = tk.StringVar(pizza)
option.set("Select an Option")
choice = tk.OptionMenu(pizza, option, "Small", "Medium", "Large")

# Lets the user check the button for the option they want
meat = tk.Checkbutton(pizza, text="Meat")
meat.grid(column=0, row=1, padx=(5, 95))
meat.configure(fg="white", bg="black")

pineapple = tk.Checkbutton(pizza, text="Pineapple")
pineapple.grid(column=0, row=3, padx=(10, 120))
pineapple.configure(fg="white", bg="black")

potato = tk.Checkbutton(pizza, text="Potato")
potato.grid(column=0, row=5, padx=(10, 120))
potato.configure(fg="white", bg="black")

# Labels for the user information
nameLabel = tk.Label(text="Name")
nameLabel.grid(column=1, row=1, padx=(10, 120))
nameLabel.configure(fg="white", bg="black")

numberLabel = tk.Label(text="Contact Number")
numberLabel.grid(column=1, row=3, padx=(5, 95))
numberLabel.configure(fg="white", bg="black")

addressLabel = tk.Label(text="Delivery Address")
addressLabel.grid(column=1, row=5, padx=(5, 95))
addressLabel.configure(fg="white", bg="black")

# Letting the user enter their information
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=2, padx=(5, 95))

numberEntry = tk.Entry()
numberEntry.grid(column=1, row=4, padx=(5, 95))

addressEntry = tk.Entry()
addressEntry.grid(column=1, row=6, padx=(5, 95))


# Defines the print function for the message board
def messageBoard():
    name = nameEntry.get()
    number = numberEntry.get()
    address = addressEntry.get()
    customer = Person(f"{name}\n{number}\n{address}")
    print(f"{customer}")

    # Message to the user
    answer = tk.Text(height=5, width=15)
    answer.grid(column=1, row=7, padx=(10, 120))
    answer.insert(tk.INSERT, f"Thank you {name} for ordering with us! Your order should be ready within 30 minutes!",
                  str(customer))


# Sets the class for customer
class Person:
    def __init__(self, name, number=None, address=None):
        self.name = name
        self.number = number
        self.address = address


# Lets you run the message board
message = tk.Button(text="Complete Order", command=messageBoard)
message.grid(column=1, row=7, padx=(5, 95))
message.configure(fg="white", bg="black")

# Puts the images into their designated spots
image1 = Image.open(
    requests.get("https://akamai.pizzahut.co.kr/2020pizzahut-prod/public/img/menu/RPPZ1546_RPEG0037_l.png",
                 stream=True).raw)
image1.thumbnail((100, 100), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
image1 = tk.Label(image=photo1)
image1.grid(column=0, row=2, padx=(5, 95))

image2 = Image.open(
    requests.get("https://akamai.pizzahut.co.kr/2020pizzahut-prod/public/img/menu/RPPZ1745_RPEG0037_l.png",
                 stream=True).raw)
image2.thumbnail((100, 100), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
image2 = tk.Label(image=photo2)
image2.grid(column=0, row=4, padx=(5, 95))

image3 = Image.open(
    requests.get("https://akamai.pizzahut.co.kr/2020pizzahut-prod/public/img/menu/RPPZ1692_RPEG0037_l.png",
                 stream=True).raw)
image3.thumbnail((100, 100), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
image3 = tk.Label(image=photo3)
image3.grid(column=0, row=6, padx=(5, 95))

# Lets the app run properly and binds the button to connect to the internet
button.bind("<Button-1>", open_url)
pizza.mainloop()
