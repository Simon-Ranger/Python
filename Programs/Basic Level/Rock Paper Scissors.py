import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    images = [rock, paper, scissors]

    userChoice = int(input("Select your choice:\n0 = rock\n1 = paper\n2 = scissors\n"))
    print(f"{images[userChoice]}")

    compChoice = random.randint(0, 2)
    print(f"The computer chose:\n{images[compChoice]}")

    if userChoice >= 3 or userChoice < 0: print(f"Invalid number...automatic loss!")
    elif userChoice == 0 and compChoice == 1: print(f"Comp Wins!!!")
    elif compChoice == 0 and userChoice == 1: print(f"You Won!!!")
    elif userChoice == 0 and compChoice == 2: print(f"You Won!!!")
    elif compChoice == 0 and userChoice == 2: print(f"Comp Wins!!!")
    elif userChoice == 1 and compChoice == 0: print(f"You Won!!!")
    elif compChoice == 1 and userChoice == 0: print(f"Comp Wins!!!")
    elif userChoice == 1 and compChoice == 2: print(f"Comp Wins!!!")
    elif compChoice == 1 and userChoice == 2: print(f"You Win!!!")
    elif userChoice == 2 and compChoice == 0: print(f"Comp Wins!!!")
    elif compChoice == 2 and userChoice == 0: print(f"You Win!!!")
    elif userChoice == 2 and compChoice == 1: print(f"You Won!!!")
    elif compChoice == 2 and userChoice == 1: print(f"Comp Wins!!!")
    elif compChoice == userChoice: print(f"No one wins...Draw!")