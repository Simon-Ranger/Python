"""
A very basic password generator that randomizes it each time the script is run, with characters ranging from 16 to 128
including all types of characters.

How to Use:
1. Run the script

Desired Output:
To have a random generated passwords appear each time the script is run.
"""

import random
import string

if __name__ == "__main__":
    characters = f"{string.ascii_letters}{string.punctuation}{string.digits}{string.hexdigits}{string.octdigits}"
    password = "".join(random.choice(characters) for i in range(random.randint(16, 200)))

    print(f"Your new randomized password is ====> {password}")

