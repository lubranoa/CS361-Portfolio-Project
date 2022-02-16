# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/16/2022
# Description: This microservice generates a password for the Password
#     Generator app's GUI by receiving a list of parameters, generating a
#     password that adheres to those parameters, and sending the password back
#     to the GUI.
# -----------------------------------------------------------------------------

import random
random.seed()


def generate_passphrase(parameters):

    passphrase = ''
    words = []

    # TODO: get specified number of words from random word generator

    # placeholder array for testing
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
