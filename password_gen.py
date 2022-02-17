# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/17/2022
# Description: This microservice generates a password for the Password
#     Generator app's GUI by receiving a list of parameters, generating a
#     password that adheres to those parameters, and sending the password back
#     to the GUI.
# -----------------------------------------------------------------------------

import random
import string

# TODO: Connect to GUI file using subprocess calls or Python slots


def generate_password(parameters):
    """
    Generates a password consisting of a specified number of characters, that
    will adhere to one or more of the following:
        - includes lowercase letters
        - includes digits
        - includes uppercase letters
        - includes a short list of special characters
        - excludes similar characters that could be mistaken for each other
        - excludes duplicate characters

    Takes a Python dictionary with data from the GUI that tells the function
    what customization to incorporate into the generated password

    Returns a generated password that adheres to the specified criteria
    """

    # TODO: Change function to handle Python dictionaries instead of arrays
    # TODO: Add functionality for minimum number of digits and minimum number
    #       of special characters

    desired_chars = ''
    password = ''

    if parameters[1] == 1:
        desired_chars = desired_chars + string.ascii_lowercase
    if parameters[2] == 1:
        desired_chars = desired_chars + string.ascii_uppercase
    if parameters[3] == 1:
        desired_chars = desired_chars + string.digits
    if parameters[4] == 1:
        desired_chars = desired_chars + '!@#$%^&*'
    if parameters[5] == 1:
        remove_chars = 'Il1O0'
        for char in remove_chars:
            desired_chars = desired_chars.replace(char, '')

    desired_chars = random.sample(desired_chars, k=len(desired_chars))
    print(desired_chars)

    while len(password) < parameters[0]:
        new_char = random.choice(desired_chars)
        if parameters[6] == 1 and new_char in password:
            print('duplicate', new_char, 'skipped')
            continue
        password = password + new_char

    print('password length:', len(password))

    return password


if __name__ == '__main__':
    pword_params = [20, 1, 1, 1, 1, 1, 1]
    pword = generate_password(pword_params)
    print(pword)
