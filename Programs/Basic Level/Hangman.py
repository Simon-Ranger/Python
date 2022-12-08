"""
This project is a simple and fun game of hangman.

How to Play:
1. When asked try to choose a letter or word

Desired Output:
Lets you vs the computer in a game of hangman

NOTE: the hangman print design is not by me, found it online and loved it...can't remember from where
"""

import random

# List of words for the game....can be changed to anything
words = ["frog", "tree", "swim", "dogs", "cats"]


def get_word(words):
    word = random.choice(words)
    return {word}


def playing(word):
    full = "_" * len(word)
    tried = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    print(f"Welcome to the Hangman Game!\n{display_hangman(attempts)}\n")

    while not tried and attempts > 0:
        guess = input('Guess a letter or word: ')

        if len(guess) == 1 and guess.isalpha():
            print(f"You have already tried {guess}!")
        elif guess not in word:
            print(f"Sorry, {guess} wasn't the word...")
            attempts -= 1
            guessed_letters.append(guess)
        elif guess in word:
            print(f"Great job, {guess} was the correct choice!")
            guessed_letters.append(guess)
            word_list = list(full)
            index = [i for i, letter in enumerate(word) if letter == guess]

            for i in index:
                word_list[i] = guess
            full = "".join(word_list)

            if "_" not in full:
                tried = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already tried {guess}!")
            elif guess != word:
                print(f"{guess} isn't the word!")
                attempts -= 1
                guessed_words.append(guess)
            else:
                tried = True
                full = word
        else:
            print(f"Invalid input\n{display_hangman(attempts)}\n{full}\n")
            if tried:
                print(f"Great job you guessed correctly!")
            elif not tried:
                print(f"No more remaining tries....The word was {word}. Better luck next time!")


def display_hangman(attempts):
    stages = ["""
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                       """,
              """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     /
                    -
                    """,
              """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |
                    -
                    """,
              """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |
                    -
                    """,
              """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |
                    -
                    """,
              """
                    --------
                    |      |
                    |      O
                    |
                    |
                    |
                    -
                    """,
              """
                    --------
                    |      |
                    |      
                    |
                    |
                    |
                    -
                    """
              ]
    return f"{stages[attempts]}"


def main():
    word = get_word(words)
    playing(word)

    while input('Play again? y/n: ') == 'y':
        word = get_word(words)
        playing(word)


if __name__ == "__main__":
    main()
