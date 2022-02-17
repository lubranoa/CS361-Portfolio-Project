# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/17/2022
# Description: This microservice generates a passphrase for the Password
#     Generator app's GUI by receiving a list of parameters, generating a
#     passphrase that adheres to those parameters, and sending the passphrase
#     back to the GUI.
# -----------------------------------------------------------------------------

# TODO: Connect to GUI using subprocess calls or Python slots
# TODO: Connect to random word generator microservice using Python slots
import random
random.seed()


def generate_passphrase(parameters):
    """
    Generates a passphrase consisting of a number of words and a selected
    separator character, and if selected, a number at the end of one word
    and/or capitalized first letters of each word.

    Takes a Python dictionary with data from the GUI that tells the function
    what customization to incorporate into the generated passphrase

    Returns a generated passphrase that adheres to the specified criteria
    """

    # TODO: Change function to handle Python dictionaries instead of lists
    # TODO: Get specified number of words from random word generator
    # TODO: Add functionality to capitalize the first letter of each word

    passphrase = ''
    # placeholder word array for testing
    words = ['aardvark', 'beaver', 'cheetah']

    random.shuffle(words)

    if parameters[2] == 1:
        word_index = random.randrange(0, len(words))
        words[word_index] = words[word_index] + str(random.randrange(0, 9))

    print(words)

    for i in range(len(words)):
        if i < 1:
            passphrase = words[i]
        else:
            passphrase = passphrase + parameters[1] + words[i]

    return passphrase


if __name__ == '__main__':

    phrase_params = [3, '@', 1]
    print(generate_passphrase(phrase_params))
