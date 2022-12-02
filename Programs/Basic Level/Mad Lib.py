"""
This is a basic program about letting the user create their own story using words and sentences of their choice.

How to Play:
1. Enter only 1 word when prompt
2. Enter a sentence, can be however long when prompt

Desired Output:
If done correctly you should end up with a story created by the previous inputs provided.
"""

if __name__ == "__main__":
    # Welcoming to the game
    print(f"Hello, welcome to Story Creator!")

    # Gathering the user inputs
    w1, w2, w3 = input('Enter a word here: '), input('Enter a word here: '), input('Enter a word here: ')
    s1, s2, s3 = input('Enter a sentence here: '), input('Enter a sentence here: '), input('Enter a sentence here: ')

    # Joining the word and sentence
    story = f"{s1} {w1}\n{s2} {w2}\n{s3} {w3}"

    # Printing the completed story
    print(f"Creating your story....\n{story}")