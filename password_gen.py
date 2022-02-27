# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 361 - Software Engineering I
# Last Modified: 02/26/2022
# Description: This microservice generates a password for the Password
#     Generator app's GUI by receiving a list of parameters, generating a
#     password that adheres to those parameters, and sending the password back
#     to the GUI.
#
# -----------------------------------------------------------------------------

import random
import string


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

    # 'len', 'low_case', 'upp_case', 'digits', 'special',
    # 'no_ambig', 'no_dup', 'min_dig', 'min_spec'
    spec_chars = '!@#$%^&*'
    remove_chars = 'Il1O0'

    desired_len = parameters['len']

    desired_chars = ''
    password_chars = []
    password = ''

    if parameters['low_case']:
        desired_chars = desired_chars + string.ascii_lowercase
    if parameters['upp_case']:
        desired_chars = desired_chars + string.ascii_uppercase
    if parameters['digits']:
        desired_chars = desired_chars + string.digits
    if parameters['special']:
        desired_chars = desired_chars + spec_chars
    if parameters['no_ambig']:
        for char in remove_chars:
            desired_chars = desired_chars.replace(char, '')

    print(desired_chars)
    desired_chars = random.sample(desired_chars, k=len(desired_chars))

    if parameters['no_dup']:
        while len(password_chars) < desired_len and len(desired_chars) > 0:
            new_char = random.choice(desired_chars)
            password_chars.append(new_char)
            desired_chars.remove(new_char)
    else:
        while len(password_chars) < desired_len and len(desired_chars) > 0:
            new_char = random.choice(desired_chars)
            password_chars.append(new_char)

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    print('password length:', len(password))

    return password


if __name__ == '__main__':
    pword_params = [20, 1, 1, 1, 1, 1, 1]
    pword = generate_password(pword_params)
    print(pword)
